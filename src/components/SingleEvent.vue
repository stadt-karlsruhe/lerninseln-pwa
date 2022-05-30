<template>

 <ion-item-group>
    <ion-item-divider>
      <ion-label class="event"><h2>{{title}}, ID {{id}}</h2></ion-label>
    </ion-item-divider>
    <ion-item color="light" >
      <ion-icon :icon="getIcon()" slot="start" class="eventIcon"/>
      <ion-label position="fixed" class="eventDate">
      <div>{{date}}</div>
      <div>{{time}}</div>
      </ion-label>
      <div>
      <ion-label class="eventMore" >
      <a :href="url" target="_blank">Mehr ...</a>
      </ion-label>
      </div>
    </ion-item>
    <ion-item-divider>
      <ion-label  class="event"><p>{{text}}</p></ion-label>
    </ion-item-divider>
 </ion-item-group>

</template>

<script lang="ts"> 
import { IonItemGroup, IonIcon, IonItem, IonItemDivider, IonLabel,
  IonPopover,
 } from '@ionic/vue';
import { volumeMuteOutline, medkitOutline, constructOutline, peopleOutline, helpOutline } from 'ionicons/icons';

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
          return volumeMuteOutline;
        case 2:
          return medkitOutline;
        case 3:
          return constructOutline;
        case 4:
          return medkitOutline;
        default:
          return helpOutline;
      } 
    }
  },
  setup() {
    return {
      volumeMuteOutline, 
      constructOutline,
      medkitOutline,
      peopleOutline,
      helpOutline,
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
  /* with position: fixed adjust size */
  flex-basis: 110px;
  margin-top: 0;
  margin-bottom: 0;
  color: #404040;
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

