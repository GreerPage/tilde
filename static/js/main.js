$(document).ready(function() {
    $("#first").click(function(){
        $("#id_img").click(); 
        return false;
    });
});
function img_pathUrl(input){
    $('#preview')[0].src = (window.URL ? URL : webkitURL).createObjectURL(input.files[0]);
    $('#preview')[0].style = "";
}