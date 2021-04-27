# And with some testing, it seems that it's here where we've reached the limits of OpenCV OCR...

# here's some JS I wrote that should help me get started..

'''
var jqry = document.createElement('script');
jqry.src = "https://code.jquery.com/jquery-3.3.1.min.js";
document.getElementsByTagName('head')[0].appendChild(jqry);
jQuery.noConflict();

function get_num() {
    console.log($('.big-number').text());
}
var test = setInterval(get_num, 1000);
'''