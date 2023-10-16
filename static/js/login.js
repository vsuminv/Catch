function loginCheck(){
    var objId = document.getElementById("user_id")
    var objPwd1 = document.getElementById("password");

    if(objId.value == ""){
        document.getElementById("id_pwError").innerHTML="아이디를 입력해주세요.";
        objId.focus();
        return false;
    }else { document.getElementById("id_pwError").innerHTML="";}

    if ((objPwd1.value) == ""){
        document.getElementById("id_pwError").innerHTML="비밀번호를 입력해주세요.";
        objPwd1.focus();
        return false;
    //비밀번호 확인을 입력 하지 않았을 경우
    } else { document.getElementById("id_pwError").innerHTML=""; }
}

function check(re,what){//정규화데이터,아이템 id,메세지
    if (re.test(what.value)) {//what의 문자열에 re의 패턴이 있는지 나타내는 함수 test
    //만약 내가 입력한 곳의 값이 정규화 데이터를 썼다면 true를 반환해서 호출 된 곳으로 리턴됨
        return true;
    }
    //alert(message);
    what.value = "";
    what.focus();
}