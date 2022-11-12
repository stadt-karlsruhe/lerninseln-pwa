<template>
  <div id="mapId">

  <l-map style="height:35vh" ref="map"
    :zoom="zoom"
    :center=selCenter 
    :max-zoom="maxZoom"
    @update:center="centerUpdate"
    @update:zoom="zoomUpdate"
  >

 <l-tile-layer 
        :url="stl0" 
        :attribution="attr0"
  >
  </l-tile-layer>

  <l-marker v-for="item in locations" :key="item.id" :lat-lng="item.latlng"
      @l-add="$event.target.openPopup()"
  >
      <l-popup 
        :content="item.Marker"
      >
      </l-popup>
      <!-- -->
      <l-icon
        :iconUrl="item.iconOptions.iconUrl"
        :iconSize="item.iconOptions.iconSize"
        >
      </l-icon>
      <!-- -->
  </l-marker>

  <l-marker v-if="posAvail" 
      :lat-lng="posMarker.latlng"
      @l-add="$event.target.openPopup()"
  >
      <l-popup 
        :content="posMarker.Marker"
      >
      </l-popup>
      <l-icon
        :iconUrl="posMarker.iconOptions.iconUrl"
        :iconSize="posMarker.iconOptions.iconSize"
        >
      </l-icon>

  </l-marker>


  
  </l-map>
  
  </div>

</template>

<script>

// leaf2vue docs: https://vue2-leaflet.netlify.app/examples/feature-group.html

// !!!! Issue with leaflet > 1.7.0:
// closing popup with href=#close breaks vue router
// !!!!

// DON'T load Leaflet components here!
// Its CSS is needed though, if not imported elsewhere in your application.
import "leaflet/dist/leaflet.css"
import { LMap, LGeoJson,LMarker, LPopup, LTileLayer, LIcon,  } from "@vue-leaflet/vue-leaflet";
import { defineComponent, ref, toRef } from 'vue';


// https://github.com/leaflet-extras/leaflet-providers
//import "leaflet-providers/leaflet-providers.js";
//http://maps.stamen.com/#terrain/12/37.7706/-122.3782

import { Geolocation } from '@capacitor/geolocation';

// ----------------------- 

//let startPnt = [49.004,  8.403]

export default defineComponent ({
  name: "LeafLet",
  props: ["reload","locations","update"],
  watch: {
    rl(a,b) {
      //alert("Reload")
      console.log("Reload",a,b)
    },
    upd(a,b) {
      console.log("Updated",a,b)
    },
    '$route' (to, from) {
      //console.log('Rout update2',to,from);
      if (to.path == "/map") {
        console.log('Now on map');
        this.updated++
        //console.log("1\n",this.$refs.map)
        //console.log("2\n",this.$refs.map.leafletObject)
        const map = this.$refs.map.leafletObject
        //this.$map.invalidateSize()
        setTimeout(function(){ map._onResize(); }, 1000);
      
      }
    },
  },
  components: {
    LMap,
    LTileLayer,
    LPopup,
    LMarker,
    LIcon,    
  },
  data() {
    return {
      geokey:0,
      zoom:12,
      maxZoom:17,
      //center1: latlng(49.004,  8.403),
      //center2: geojsonOptions.latlng(49.004,  8.403),
      //center: this.geojsonOptions.latlng(49.004,  8.403),
      center: [49.004,  8.403],
      //url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      /*
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
        */
      markers : [],
      geojson: {},
      geojsonOptions: {
        /*
        "crs": {
          "type": "name",
          "properties": {
            "name": "EPSG:4326"
          }
        },
        */
      },
      updated: 0,
      // 2022: no {s} on on osm tiles any more
      //stl0: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      stl0: "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
      stl1: "https://stamen-tiles.a.ssl.fastly.net/toner/{z}/{x}/{y}.png",
      stl2: "https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg",
      stl3: "https://stamen-tiles.a.ssl.fastly.net/watercolor/{z}/{x}/{y}.jpg",
      attr0: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      attr1: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
      attr2: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://www.openstreetmap.org/copyright">ODbL</a>.',
      attr3: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.',
    };
  },
  computed: {
    selCenter() {
      // https://v3.vuejs.org/guide/computed.html#computed-properties
      const center = [49.004,  8.403]
      //if (!this.mapIsReady) 
      return center
    },
  },
  methods : {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
    async initialize() {
      // start location search
      Geolocation.getCurrentPosition().then(geoLoc => {
        const pnt =  [geoLoc.coords.latitude,geoLoc.coords.longitude]
        console.log('Current position:', geoLoc,pnt);
        const content = '<div class="popInfo"><h3>Du bist hier!</h3></div>'
        const iconUrl = "/assets/img/map/bulb.png"
        const iconSize = [32,32] 
        const iconOptions = {"iconUrl":iconUrl,"iconSize":iconSize}
        this.posMarker = {"latlng":pnt,
        "Marker":content,
        "iconOptions":iconOptions}
        this.posAvail = true
      });

    }
  },
  async beforeMount() {

    // HERE is where to load Leaflet components!
    //const { map, marker, tileLayer, markerLayer, LayerGroup, latLng } = await import("leaflet/dist/leaflet-src.esm");
    const { latLng } = await import("leaflet/dist/leaflet-src.esm");
    //const { LMarker, LPopup, LTileLayer } = await import("leaflet/dist/leaflet-src.esm");

    const kaLat = {
      "center": 49.004,
      "min": 48.96,
      "max": 49.0391
    };
    const kaLon = {
      "center": 8.403,
      "min": 8.325,
      "max": 8.49
    };


    // And now the Leaflet circleMarker function can be used by the options:
    //this.geojsonOptions.pointToLayer = (feature, latLng) =>
     // circleMarker(latLng, { radius: 8 });
    //this.geojsonOptions.latlng = (lat, lon) => latLng(lat,lon);
    this.latLng = (lat, lon) => latLng(lat,lon);

    this.startPnt = [49.004,  8.403]

    this.mapIsReady = true;
 
    await this.initialize();
  },
  // store
  setup(props) {
    const posAvail = ref(false)
    const posMarker = ref({})
    const rl = toRef(props, 'reload')
    const upd = toRef(props, 'update')
    return { rl, posMarker, posAvail, upd };
  },

});


</script>

<style scoped>
  .popInfo {
    font-weight: bold;
  }
  .popInfo h3{
    font-size: 1.3rem;
  }
</style>

<style>
.leaflet-marker-icon  {
    border: 2px solid black;
    border-radius:10px;
  }

.leaflet-popup-content p {
  margin: unset;
}
</style>