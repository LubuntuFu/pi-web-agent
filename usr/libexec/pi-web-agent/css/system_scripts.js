function navigate(link) {
     thumbnailviewer.closeit();
     //$(".span16").prepend(animationBar());
     //$(".span16").load(link);
     //window.history.pushState({}, "", link.split("?")[0]);
     $('#dialog_window_1').dialog();
     $("#dialog_window_1").load(link);
     
     
}



function animationBar() {
    return '<div id="b-pb" class="progress progress-striped active"><div class="progress-bar" style="width: 100%"></div></div>'
}

function check_for_updates() {
    $(".span16").prepend(animationBar());
    $("#check_button").remove()
    getResponse('/cgi-bin/toolkit/live_info.py?cmd=check_app', update_check_completed) 
}

function update_app() {
    $(".span16").prepend(animationBar());
    $("#update_button").remove()    
    getResponse('/cgi-bin/toolkit/live_info.py?cmd=update_app', update_response)
    
}

function update_response(response) {
    if (response == "0")
        check_for_updates();
    else
        $("#updates").append('Update failed. Please try again later');
    $("#b-pb").remove()
}
function update_check_completed(info) {
    
    if (info.length <= 5) {
        $("#updates").append('Application is in its latest version')
    }
    else {
        $("#updates").append('<button class="btn btn-info" type="button" onclick="update_app()" id="update_button">Update</button>')
    }
    $("#b-pb").remove()

}

function start_live_streaming() {
    getResponse('/cgi-bin/toolkit/camera.py?cmd=start', sls)
}

function sls(info) {
    return;
}

function stop_live_streaming() {
    getResponse('/cgi-bin/toolkit/camera.py?cmd=stop', sls)
}
