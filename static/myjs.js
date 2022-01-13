 //**로그아웃 기능 : 메인+상세 **//
        function sign_out() {
            // 로그아웃 버튼을 누른 해당 유저의 토큰을 삭제
            $.removeCookie('mytoken', {path: '/'})
            alert('로그아웃!')
            // 로그아웃 후 로그인 페이지로 이동
            window.location.href = "/login"
        }



// 좋아요 함수
function toggle_like(post_id, type) {
            // 좋아요 버튼 태그를 찾는 과정
            let $a_like = $(`#${post_id} a[aria-label=${type}]`)
            let $i_like = $a_like.find("i")
            if ($i_like.hasClass("fa-thumbs-up")) {
                // 좋아요 아이콘이 채워져 있는 상태에서 눌렀다면, 좋아요 취소 행동이라고 서버에 보냄
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
                        // 채워져있던 아이콘 비우는 class 추가
                        $i_like.addClass("fa-thumbs-o-up").removeClass("fa-thumbs-up")
                        // 좋아요 수 표시하는 태그 속 텍스트 바꾸기
                        $a_like.find("span.like-num").text(num2str(response["count"]))
                        window.location.reload()
                    }
                })
            } else {
                // 좋아요 아이콘이 채워지지 않은 상태에서 눌렀다면, 좋아요 행동이라고 서버에 보냄
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

// 좋아요 숫자 형식 : 큰 숫자가 되면 형태 바뀜 + 0은 표시 안함
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