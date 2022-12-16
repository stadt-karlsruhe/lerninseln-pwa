<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title >Lerninseln
        <img alt="logo" height="40" style="vertical-align:middle"  src="/assets/img/logo.png" > 
        </ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true" >
    <div ref="tab1" class="swiping">
    
    <IntroText></IntroText>
    <!--    
    <LoginForm></LoginForm>
    -->

    <!--
    <IntroSlides v-if="!loading" ></IntroSlides>
    -->

    <ProviderList></ProviderList>

    <ImPrint></ImPrint>

    </div>
    </ion-content>
  </ion-page>
</template>

<script lang="js">
import { IonPage, IonHeader, IonToolbar, IonTitle, IonContent,  } from '@ionic/vue';

import { defineComponent, ref } from 'vue'; 

//import ExploreContainer from '@/components/ExploreContainer.vue';
//import LoginForm from '@/components/LoginForm.vue';
import IntroText from '@/components/IntroText.vue';
import IntroSlides from '@/components/IntroSlides.vue';
import ProviderList from '@/components/ProviderList.vue';
import ImPrint from '@/components/ImPrint.vue';

import { createGesture } from '@ionic/vue';
import router from "../router";


export default  defineComponent ({
  name: 'IntroView',
  components: { //LoginForm, 
    IntroText, ProviderList, IonHeader, IonToolbar, IonTitle, 
    IonContent, IonPage, ImPrint, //IntroSlides,
  },
  data: function() {
    return {
    } 
  },
  watch: {
    '$route' (to, from) {
      if (to.path == "/intro") {
        console.log('Now on intro');
      }
    }
  },
  methods : {
    onSwipe(detail) {
      const type = detail.type;
      const cx = detail.currentX;
      const dx = detail.deltaX;
      const vx = detail.velocityX;
      //console.log(type,cx,dx,vx)
      //if ((type == "pan") && (dx > 100) && (vx > 1)) router.push("/tabs/tab3")
      if ((type == "pan") && (dx < -100) && (vx < -1)) router.push("/map")
    },
  },
  async beforeMount() {
    // moved to mapview
  },
  async mounted(){
    const gest = this.$refs.tab1 //ref();
    // const r = router.currentRoute.value.path // value is important!
    //console.log("Current: ",r,"ref2:",gest)
    //setTimeout(function(){console.log(r.path)},2000)
    const gesture = createGesture({
      onMove: (detail) => { this.onSwipe(detail);},
      gestureName: 'swipe',
      el: gest,
    })
    gesture.enable();
  },
  setup() {
    return {  };
  }
})

</script>


<style scoped>

ion-toolbar {
  /* https://ionicframework.com/docs/api/toolbar */
  /* background color from app.vue */
  --border-color:#048500;
  --border-width:3px;
  --border-style:solid none none none;
}

/* https://stackoverflow.com/questions/54956372/how-to-change-the-toolbar-color-in-ionic-4 

*/

.loader-class {

}

/* can overwrite here ... **
ion-content {
    --background: url('/assets/img/bg/backIcons_white.png');
    --background-repeat: repeat;
}
*/

/*
.ion-page {
  max-width:960px;
  margin-left:auto;
  margin-right:auto;
}
*/
.swiping {
  min-height:90%;
}

</style>
