<template>

 <ion-item-group>
    <ion-item-divider>
    </ion-item-divider>
    <ion-item color="light" >
      <ion-icon :icon="getIcon()" slot="start" class="eventIcon"/>
      <ion-label position="inline" class="eventDate">
        <span class="eventTitle">{{title}}</span>
            <a class="eventMore"  :href="url" target="_blank">Mehr ...</a>
      </ion-label>
    </ion-item>
 </ion-item-group>

</template>

<script lang="ts"> 
import { IonItemGroup, IonIcon, IonItem, IonItemDivider, IonLabel,
  IonPopover,
 } from '@ionic/vue';
import {   
  volumeMuteOutline,
  medkitOutline,
  constructOutline,
  peopleOutline,
  albumsOutline,
  telescopeOutline,
  wifiOutline,
  desktopOutline,
  contractOutline,
  syncOutline,
  trophyOutline,
  rocketOutline,
 } from 'ionicons/icons';

import Popver from './popover.vue'

// could use thumbnails or avatars in place of icons.
/*
https://ionicframework.com/docs/api/thumbnail
<ion-thumbnail>
    <img src="https://gravatar.com/avatar/dba6bae8c566f9d4041fb9cd9ada7741?d=identicon&f=y">
  </ion-thumbnail>

https://ionicframework.com/docs/api/avatar

*/

import { defineComponent } from 'vue'; 

export default defineComponent({
  props: ['title','text',"date",'time','id','icon',"url"],
  components: {IonItemGroup, IonIcon, IonItem, IonItemDivider, IonLabel,
    },
  data () {
    return {
      popOpen: false,
    }
  },
  methods: {
    popState(v: boolean) {
      this.popOpen = v
      console.log("Close:",v)
    },
    getIcon(){
      //console.log("Icon id:",parseInt(this.icon))
      switch (parseInt(this.icon)) {
        case 1:
          return desktopOutline;
        case 2:
          return constructOutline;
        case 3:
          return peopleOutline;
        case 4:
          return rocketOutline;
        default:
          return telescopeOutline;
      } 
    }
  },
  setup() {
    return {
      volumeMuteOutline,
      medkitOutline,
      constructOutline,
      peopleOutline,
      albumsOutline,
      telescopeOutline,
      wifiOutline,
      desktopOutline,
      contractOutline,
      syncOutline,
      trophyOutline,
      rocketOutline,
    }
  }
});

</script>

<style scoped>

h2 {
  padding-bottom: .2rem;
}

.eventPop {
  width: 100%;
}

.popover-content {
  width:600px;
}
.event {
  text-align: left;
  white-space: normal;
  margin-top: 0;
  margin-bottom: 0;
}

.eventIcon {
  margin-right: .5em;
}

.eventDate {
  text-align: left;
  /* with position: fixed adjust size *
  flex-basis: 10px;
  */
  margin-top: 0;
  margin-bottom: 0;
  color: #404040;
}

.eventTitle {
  font-size: 120%;
  margin-right: 1em;
}

.eventMore {
  text-align: left;
  /* with position: fixed adjust size */
  display: inline-block;
  text-decoration-line: underline;
  text-decoration-color: primary;
  color: primary;
}

.eventMore:hover {
    cursor:pointer;
}

.footer {
  height: 1rem;
  background-color: primary;

}
</style>

