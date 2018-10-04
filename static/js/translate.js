// Customize the Google Translate dropdown style

 // (A bit tricky as the dropdown is wrapped in an iframe asynchronously loaded)

(function() {

   var $previewFrame = $('#preview-frame');


   function restyleDropdown() {


     // In case of Zendesk preview mode, another iframe is wrapping the whole page

     var $dropdownIframe = $previewFrame.length === 1

    ? $previewFrame.contents().find('.goog-te-menu-frame.skiptranslate')

    : $('.goog-te-menu-frame.skiptranslate');

     if($dropdownIframe.length) {

      $dropdownIframe

         .contents()

         .find('head')

         .append('<link rel="stylesheet" type="text/css" href="//p4.zdassets.com/hc/theme_assets/549775/200068704/google-translate-override.css"/>');

     } else {

      setTimeout(restyleDropdown, 100);

     }

   }

   restyleDropdown();

})();