<template>

  <ion-slides ref="slider" class="slides" pager="false" 
    :options="slideOpts" 
    @ionSlidesDidLoad="slidesLoaded" 
    >
    <ion-slide>
     <ion-img class="frontImg" src="/assets/img/front/1.jpg"></ion-img>
    </ion-slide>
    <ion-slide>
     <ion-img class="frontImg" src="/assets/img/front/2.jpg"></ion-img>
    </ion-slide>
    <ion-slide>
     <ion-img class="frontImg" src="/assets/img/front/3.jpg"></ion-img>
    </ion-slide>
  </ion-slides>


</template>

<script> 
import { IonImg, IonSlides, IonSlide } from '@ionic/vue';

import { defineComponent } from 'vue';


// maybe check https://thewebdev.info/2021/01/10/add-a-swiper-carousel-into-a-vue-3-app-with-swiper-6/
// and https://swiperjs.com/vue
// https://www.youtube.com/watch?v=-Qm-tG4Kt9s

export default defineComponent({
  name: "IntroSlides",
  watch: {
    '$route' (to, from) {
      //console.log('Rout update2',to,from);
      if (from.path == "/intro") {
        if (this.sliderLoaded) {
          this.$refs.slider.$el.stopAutoplay().then(() => {console.log("Autoplay stopped")})
        }
        console.log('Leaving');
      }
      if (to.path == "/intro") {
        console.log('Now on intro');
        if (this.sliderLoaded) {
          this.$refs.slider.$el.startAutoplay().then(() => {console.log("Autoplay started")})
        }
      }
    }
  },
  components: { IonSlides, IonSlide, IonImg,
  },
  data : function() {
    return {
        sliderLoaded:false,
        updated: 0,
    }
  },
  methods: {
    /*
    @ionSlideDidChange="slideChanged($event)" 
    @ionSlideNextStart="slideNext($event)" 
    slideChanged(event) {
      console.log("Changed:",event)
    },
    slideNext(event) {
      console.log("Next:",event)
    }
    */
    async slidesLoaded() {
      console.log("Slides Loaded") //,event.target)
      // autoplay is set on option, don't need to do this here again
      //await this.$refs.slider.$el.startAutoplay()
      //await this.$refs.slider.$el.lockSwipes(true)
      this.sliderLoaded = true
      /*
      console.log("Swiper",swiper)
      const index = await this.$refs.slider.$el.getActiveIndex()
      console.log("Index",index)
      //await this.$refs.slider.$el.slideTo(2)
      */
      // await this.$refs.slider.$el.startAutoplay()


      
      /*
      const swiper = this.$refs.slider
      const s1 = new IonSlides.Slides().getSwiper()
      console.log("Swiper",s1)
      console.log("slider: ",swiper)
      console.log("swiper: ",swiper.swiper)
      console.log("swiper: ",swiper.getSwiper)
      console.log("swiper: ",this.swiper)
      const s1 = swiper.getSwiper()
      const s2 = IonSlides.getSwiper()
      */
    },
  },
  setup(){
      const slideOpts = {
            initialSlide: 0,
            // multiple per view
            //slidesPerView: 2,
            spaceBetween: 20,
            speed: 1200,
            //watchSlidesProgress: true,
            autoplay: true, // 2500
            loop: false,
      }
    return { slideOpts}
  }
});

</script>

<style scoped>

.slides {
}

.vueslide {
  max-height:300px;
}

.vueslides {
}

.frontImg {
  max-width:400px;
  padding-left:1em;
  padding-right:1em;
  
}

</style>

