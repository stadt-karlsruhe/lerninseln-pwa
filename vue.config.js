module.exports = {
    // ----- from ionic docs . OK ???
    chainWebpack: (config) => {
      config.plugins.delete('prefetch');
      config.plugin('workbox') // for pwa. needed?
    },
    // ----------------------
    pwa: {
      name: 'LerninselnPWA',
      themeColor: '#4DBA87',
      //msTileColor: '#000000',
      //appleMobileWebAppCapable: 'yes',
      //appleMobileWebAppStatusBarStyle: 'black',
      // detailed manifest options must go into manifestOptions!
      // configure the workbox plugin
      workboxPluginMode: "GenerateSW", //'InjectManifest',
      workboxOptions: {
        // swSrc is required in InjectManifest mode.
        //swSrc: 'dev/sw.js',
        // ...other Workbox options...
      },
      manifestOptions:{
        short_name: 'LiPwa',
        start_url: "/intro",
        display: "standalone",
        background_color: "#eeeeee",
        //msTileColor: '#000000',
        msTileColor: '#eeeeee',
        appleMobileWebAppCapable: 'yes',
        appleMobileWebAppStatusBarStyle: 'black',
        mobileWebAppCapable: 'yes',
          icons: [
          {
            "src": "/img/icons/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
          },
          {
            "src": "/img/icons/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
          },
          {
            "src": "/img/icons/android-chrome-maskable-192x192.png",
            "sizes": "192x192",
            "type": "image/png",
            "purpose": "maskable"
          },
          {
            "src": "/img/icons/android-chrome-maskable-512x512.png",
            "sizes": "512x512",
            "type": "image/png",
            "purpose": "maskable"
          },
          {
            "src": "/img/icons/apple-touch-icon-60x60.png",
            "sizes": "60x60",
            "type": "image/png"
          },
          {
            "src": "/img/icons/apple-touch-icon-76x76.png",
            "sizes": "76x76",
            "type": "image/png"
          },
          {
            "src": "/img/icons/apple-touch-icon-120x120.png",
            "sizes": "120x120",
            "type": "image/png"
          },
          {
            "src": "/img/icons/apple-touch-icon-152x152.png",
            "sizes": "152x152",
            "type": "image/png"
          },
          {
            "src": "/img/icons/apple-touch-icon-180x180.png",
            "sizes": "180x180",
            "type": "image/png"
          },
          {
            "src": "/img/icons/apple-touch-icon.png",
            "sizes": "180x180",
            "type": "image/png"
          },
          {
            "src": "/img/icons/favicon-16x16.png",
            "sizes": "16x16",
            "type": "image/png"
          },
          {
            "src": "/img/icons/favicon-32x32.png",
            "sizes": "32x32",
            "type": "image/png"
          },
          {
            "src": "/img/icons/msapplication-icon-144x144.png",
            "sizes": "144x144",
            "type": "image/png"
          },
          {
            "src": "/img/icons/mstile-150x150.png",
            "sizes": "150x150",
            "type": "image/png"
          }
        ]
      },
    },    
  };
