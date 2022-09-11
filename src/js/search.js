// for use in lifeprint/search/index
function keyWordsearch(e, t) { res = e; for (var n = 0; n < t.length; n++) { res = res.replace(/\{\{(.*?)\}\}/g, function (e, r) { return t[n][r] }) } return res }

$(function () {
    $("form").on("submit", function (e) {
        e.preventDefault();
        // prepare the request
        var request = gapi.client.youtube.search.list({
            part: "snippet",
            type: "video",
            q: encodeURIComponent($("#search").val()).replace(/%20/g, "+"),
            maxResults: 50,
            order: "title",
            channelId: "UCZy9xs6Tn9vWqN_5l0EEIZA"
        });
        // execute the request
        request.execute(function (response) {
            var results = response.result;
            $("#results").html("");
            $.each(results.items, function (index, item) {
                $.get("tpl/item.htm", function (data) {
                    $("#results").append(keyWordsearch(data, [{ "title": item.snippet.title, "videoid": item.id.videoId }]));
                });
            });
            resetVideoHeight();
        });
    });

    $(window).on("resize", resetVideoHeight);
});

function resetVideoHeight() {
    $(".video").css("height", $("#results").width() * 9 / 16);
}

function init() {
    gapi.client.setApiKey("AIzaSyAEsGEeR6rBzhXiwSkzLFF1GFJwW3Cm810");
    gapi.client.load("youtube", "v3", function () {
        // yt api is ready
    });
}
//<!--GET https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCZy9xs6Tn9vWqN_5l0EEIZA&maxResults=10&order=title&q=take&key={YOUR_API_KEY}>