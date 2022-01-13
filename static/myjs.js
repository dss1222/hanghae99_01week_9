
function toggle_like(post_id, type) {
            let $a_like = $(`#${post_id} a[aria-label=${type}]`)
            let $i_like = $a_like.find("i")
            if ($i_like.hasClass("fa-thumbs-up")) {
                $.ajax({
                    type: "POST",
                    url: "/update_like",
                    data: {
                        post_id_give: post_id,
                        type_give: type,
                        action_give: "unlike"
                    },
                    success: function (response) {
                        console.log("unlike")
                        $i_like.addClass("fa-thumbs-o-up").removeClass("fa-thumbs-up")
                        $a_like.find("span.like-num").text(num2str(response["count"]))
                        window.location.reload()
                    }
                })
            } else {
                $.ajax({
                    type: "POST",
                    url: "/update_like",
                    data: {
                        post_id_give: post_id,
                        type_give: type,
                        action_give: "like"
                    },
                    success: function (response) {
                        console.log("like")
                        $i_like.addClass("fa-thumbs-up").removeClass("fa-thumbs-o-up")
                        $a_like.find("span.like-num").text(num2str(response["count"]))
                        window.location.reload()
                    }
                })

            }
        }

// 좋아요 숫자 형식
function num2str(count) {
    if (count > 10000) {
        return parseInt(count / 100) + "k"
    }
    if (count > 500) {
        return parseInt(count / 100) / 10 + "k"
    }
    if (count == 0) {
        return ""
    }
    return count
}