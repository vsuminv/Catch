$('.before_text').keyup(function (e){
    var content = $(this).val(); //입력한 것
    $('#counter').html("("+content.length+" / 최대 500자)");  //글자수 카운팅

    if (content.length > 200){ //200자 이상일 때
        alert("최대 200자까지 입력 가능합니다.");
        $(this).val(content.substring(0, 500)); //넘어간 글자 자르기
        $('#counter').html("(500 / 최대 500자)");
    }
}); 