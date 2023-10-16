
//사이트 나가기, 새로고침 안내창
var checkUnload = true;
$(window).on('beforeunload', function () {
    if (checkUnload) return "이 페이지를 벗어나면 작성된 내용은 저장되지 않습니다.";
});
$("#style-btn").on("click", function () {
    checkUnload = false;
    $("submit").submit();
});


// if(!$('#expected > option:selected').val()) {
//     alert("아나 선택 좀..");
// }

// if($("#expected").val() == ''){
//     alert('test')
//     return false;

// }

function check(){
    if($("#expected").val() == ''){
        alert('진행 방식을 선택해 주세요.')
        return false;
    }

    if($("#people").val() == ''){
        alert('모집 인원을 선택해 주세요.')
        return false;
    }
    if($("#start_date").val() == ''){
        alert('시작 예정일을 선택해 주세요.')
        return false;
    }

    if($("#month").val() == ''){
        alert('예상 기간을 선택해 주세요.')
        return false;
    }

    if($("#tag").val() == ''){
        alert('관심 태그를 입력해 주세요.')
        return false;
    }

    if($("#due_date").val() == ''){
        alert('모집 기간을 선택 해주세요.')
        return false;
    }
}