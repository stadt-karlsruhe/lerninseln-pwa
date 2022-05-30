<template>
    <ion-item-group class="filter">
    <!--
    <ion-item class="filterItem"  lines="none">
          <ion-label class="filterLabel">{{name}}</ion-label>
    </ion-item>
    -->

    <!--
        @ionChange="toppings.value.push($event.target.value)"
        value="pepperoni"
        :checked="toppings.value.indexOf('pepperoni') !== -1">

... from check box
          @update:modelValue="checked = $event"
            :modelValue="check"

        .. works almos but toggles too much...
          :checked=check
          
          @ionChange="filter()" 

    -->

    <ion-item lines="none">
            <ion-icon :icon=icon class="filterIcon" @click="iconHelp"/>
    </ion-item>
    <ion-item class="filterToggle" lines="none">
          <ion-checkbox
          @update:modelValue="{checked = $event;filter()}"
          :modelValue="checked"
          >
          </ion-checkbox>
    </ion-item>
    
    </ion-item-group>
</template>

<script lang="ts">
import {IonCheckbox, IonIcon, IonItemGroup, IonItem } from '@ionic/vue';

import { IonButton, IonPopover, popoverController } from '@ionic/vue';
import { defineComponent, ref } from 'vue';

import FilterInfo from "./FilterInfo.vue"


export default defineComponent ({
  name: "FilterItem",
  components: { IonCheckbox, IonIcon, IonItemGroup, IonItem, 
  },
  data () {
    return {
      checked: this.check,
    }
  },
  props: {
    "name": String,
    "info": String,
    "icon": IonIcon,
    "check": Boolean
  },
  emits: ['filter'],
  methods: {
    filter(){
      console.log("F1:", this.name," - ",this.check, this.checked, this.info)
      if (this.checked) {
        this.$emit("filter",true)
      } else {
        this.$emit("filter",false)
      }
    },
    async iconHelp(ev: Event) {
      console.log("help")
      const popover = await popoverController
        .create({
          component: FilterInfo,
          componentProps: {"info":this.info},
          cssClass: 'filterInfoClass',
          event: ev,
          translucent: true
        })
      await popover.present();
      const { role } = await popover.onDidDismiss();
      console.log('onDidDismiss resolved with role', role);
    },

  },
  
  watch: {
    "check": function (a,b) { 
        console.log(this.name," : ",a,b)
        this.checked = a
    }
  },

});
</script>

<style scoped>

.hdr {
  color: unset;  
}

.center {
  text-align: center;

}

.label {

}

.filter {
  display: inline-block;
  max-width:18%;
}

.filterLabel {
  text-align: center;

}

.filterIcon {
  text-align: center;
  margin-left:auto;
  margin-right:auto;
  width:100;
  background: #fff;
  border-bottom: solid 4px #5260ff; 
}

.filterToggle {
  text-align: center;
}


ion-item {
  --padding-start: 15px;
  --inner-padding-end: 5px;
  --min-height: 30px;
}

.in-item {
  margin-inline: 0;
}

</style>
