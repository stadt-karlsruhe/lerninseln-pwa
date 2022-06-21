vue-pwa-asset-generator
https://dev.to/jcalixte/vuejs-pwa-assets-generator-4jhn
https://www.npmjs.com/package/vue-pwa-asset-generator

or maybe 

https://itnext.io/pwa-splash-screen-and-icon-generator-a74ebb8a130
https://github.com/onderceylan/pwa-asset-generator


pwa instllation, local storage and caching:
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Client-side_storage
https://github.com/mdn/learning-area/tree/main/javascript/apis/client-side-storage/cache-sw/video-store-offline
https://developers.google.com/web/fundamentals/codelabs/offline/
https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API/Using_the_Web_Storage_API
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Installable_PWAs
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Add_to_home_screen


pwa push + notification:
https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Re-engageable_Notifications_Push
https://developer.mozilla.org/en-US/docs/Web/API/Push_API
https://blog.mozilla.org/services/2016/08/23/sending-vapid-identified-webpush-notifications-via-mozillas-push-service/


periodic background sync:
https://developer.mozilla.org/en-US/docs/Web/API/Web_Periodic_Background_Synchronization_API
https://github.com/mdn/content/blob/main/files/en-us/web/api/web_periodic_background_synchronization_api/

XSRF
When a user visits a site, the site should generate a (cryptographically strong) pseudorandom value and set it as a cookie on the user's machine. The site should require every form submission to include this pseudorandom value as a form value and also as a cookie value. When a POST request is sent to the site, the request should only be considered valid if the form value and the cookie value are the same. When an attacker submits a form on behalf of a user, he can only modify the values of the form. An attacker cannot read any data sent from the server or modify cookie values, per the same-origin policy. This means that while an attacker can send any value he wants with the form, he will be unable to modify or read the value stored in the cookie. Since the cookie value and the form value must be the same, the attacker will be unable to successfully submit a form unless he is able to guess the pseudorandom value. 
https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#token-based-mitigation
https://infosec.mozilla.org/guidelines/web_security#csrf-prevention
Inserting the CSRF token in the custom HTTP request header via JavaScript is considered more secure than adding the token in the hidden field form parameter because it uses custom request headers.


