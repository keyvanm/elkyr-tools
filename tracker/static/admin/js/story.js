var jQuery = django.jQuery;
var $ = jQuery;

$(function () {
    $("td.field-state:contains('Finished')").parent().addClass('finished-story');
});
