module.exports = {
    // ----- from ionic docs . OK ???
    chainWebpack: (config) => {
      config.plugins.delete('prefetch');
    },
    // ----------------------
    pwa: {
        name: 'Lerninseln',
        themeColor: '#ffffff',
        msTileColor: '#000000',
        appleMobileWebAppCapable: 'yes',
        appleMobileWebAppStatusBarStyle: 'white',
   
      },    
  };
