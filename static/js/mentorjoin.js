function validate() {
    //event.preventDefault();
    var objPwd1 = document.getElementById("password");
    var objPwd2 = document.getElementById("passwordCheck");
    var objEmail = document.getElementById("email");
    var objName = document.getElementById("name");
    var objNickname = document.getElementById("nickname");
    var objCellphone = document.getElementById("tel");
    var objBirthday = document.getElementById("birthday")
    var objMale = document.getElementById("male")
    var objFemal = document.getElementById("female")
    var objId = document.getElementById("user_id")
    var objidCheck = document.getElementById("id_check");
    var objDepartment = document.getElementById("department"); 
    // var objUniversity = document.getElementsByName("university");
    var objUniversity = document.getElementById("university");
    var objStudentId = document.getElementById("student_Id");
    var objAttending = document.getElementById("attending");
    var objTitle = document.getElementById("title");
    var objDescription = document.getElementById("description");
    



    //패스워드 값 데이터 정규화 공식
    // var regul1 = /^[a-zA-Z0-9]{4,12}$/;
    // 8 ~ 16자 영문, 숫자, 특수문자를 최소 한가지씩 조합
    var regul1 = /^(?=.*[a-zA-z])(?=.*[0-9])(?=.*[$`~!@$!%*#^?&\\(\\)\-_=+]).{8,16}$/;

    //이메일 정규화 공식
    // var regul2 = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$/;
    //var regul2 = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/;
    var regul2 = /^[a-z0-9]+@[a-z]+\.[a-z]{2,3}$/;
    //이름 정규화 공식
    var regul3 = /^[가-힣]{2,10}$/;
    //닉네임 정규화 공식
    // var regul4 = /^[가-힝a-zA-Z]{2,}$/;
    // var regul4 = /^([a-zA-Z0-9ㄱ-ㅎ|ㅏ-ㅣ|가-힣]).{1,10}$/
    var regul4 =  /^[ㄱ-ㅎ|가-힣|a-z|A-Z|0-9|]+$/
    //전화번호 정규화 공식
    // var regul5 = /(\d{3})(\d{4})(\d{4})$/;
    var regul5 = /^01(?:0|1|[6-9])(?:\d{4})\d{4}$/;
    // 생년월일 정규화 공식
    var regul6 = /^(19[0-9][0-9]|20\d{2})(0[0-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])$/;
    //학과 정규화 공식
    var regul7 = /^([0-9]{2} ) + 학번/;



    //이름 입력 안 한 경우
    if ((objName.value)=="") {
        document.getElementById("nameError").innerHTML="이름을 입력해주세요.";
        objName.focus();
        return false;
    } else { document.getElementById("nameError").innerHTML="";}
    //이름에 영어나 특수 문자가 들어 간 경우
    if (!check(regul3,objName,)) {
        document.getElementById("nameError").innerHTML="잘못된 형식의 이름입니다.";
        return false;
    }


    //닉네임 입력 안 한 경우
    if(objNickname.value == ""){
    document.getElementById("nicknameError").innerHTML="닉네임을 입력해주세요.";
    objNickname.focus();
    return false;
    } else { document.getElementById("nicknameError").innerHTML="";}
    
    //닉네임에 특수 문자가 들어간 경우
    if (objNickname.value.length < 2 || objNickname.value.length > 10) {
        document.getElementById("nicknameError").innerHTML="2자 이상 10자 이하만 입력해주세요.";
        objNickname.focus();
        return false;
    }else if(!check(regul4,objNickname)){
        document.getElementById("nicknameError").innerHTML="한글, 영어, 숫자만 입력해주세요.";
        return false;
    }else { document.getElementById("nicknameError").innerHTML="";}

    //전화번호 입력 안 한 경우
    if ((objCellphone.value)=="") {
        document.getElementById("telError").innerHTML="전화번호를 입력해주세요.";
        objCellphone.focus();
        return false;
    } else { document.getElementById("telError").innerHTML="";}
    // 전화번호 형식이 잘못된 경우
    if (!check(regul5,objCellphone)) {
        document.getElementById("telError").innerHTML="잘못된 형식의 전화번호입니다.";
        return false;
    }

    //생년월일 입력 안 한 경우
    if ((objBirthday.value)=="") {
        document.getElementById("birthdayError").innerHTML="생년월일을 입력해주세요.";
        objBirthday.focus();
    return false;
    } else { document.getElementById("birthdayError").innerHTML=""; }

    //생년월일이 잘못된 경우
    if (!check(regul6,objBirthday)) {
        document.getElementById("birthdayError").innerHTML="잘못된 형식의 생년월일입니다.";
        return false;
    } else { document.getElementById("birthdayError").innerHTML=""; }


    if(!objMale.checked && !objFemal.checked ){
        console.log(!objMale.value, objFemal.value)
        document.getElementById("genderError").innerHTML="성별을 체크해주세요.";
        // objMale.focus();
        // objFemal.focus();
        return false;
     }else {document.getElementById("genderError").innerHTML=""}


    //아이디 작성 안 했을 경우
    if(objId.value == ""){
        document.getElementById("user_idError").innerHTML="아이디를 입력해주세요.";
        objId.focus();
        return false;
    }else { document.getElementById("user_idError").innerHTML="";}
    //아이디 형식 잘못된 경우
    if (!check(regul2,objId)) {
        document.getElementById("user_idError").innerHTML="잘못된 형식의 이메일입니다.";
        return false;
    }

    // 아이디 중복검사 안 했을 때
    // if(!objidCheck.value == ""){
    //     document.getElementById("user_idError").innerHTML="아이디 중복검사를 해주세요.";
    //     objidCheck.focus();
    //     return false;
    // }else{document.getElementById("user_idError").innerHTML="";}

    if(objId.value == 'true' ){
        document.getElementById("user_idError").innerHTML="이미 존재하는 아이디입니다.";
        objId.focus();
        return false;
    }else{
        document.getElementById("user_idError").innerHTML="";        
    }  

    //비밀번호 입력 하지 않았을 경우
    if ((objPwd1.value) == ""){
        document.getElementById("passwordError").innerHTML="비밀번호를 입력해주세요.";
        objPwd1.focus();
        return false;
    //비밀번호 확인을 입력 하지 않았을 경우
    } else { document.getElementById("passwordError").innerHTML=""; }
    //비밀번호 유효성 검사
    if (!check(regul1,objPwd1)) {
        document.getElementById("passwordError").innerHTML="비밀번호는 8 ~ 16자 영문, 숫자, 특수문자를 최소 한가지씩 조합해주세요.";
        return false;
    } else { document.getElementById("passwordError").innerHTML="";}

    if ((objPwd2.value=="")){
        document.getElementById("passwordCheckError").innerHTML="비밀번호 확인을 입력해주세요.";
        objPwd2.focus();
        return false;
    } else { document.getElementById("passwordCheckError").innerHTML="";}

    //비밀번호와 비밀번호 확인이 일치 하지 않을 경우
    if ((objPwd1.value)!=(objPwd2.value)) {
        document.getElementById("passwordCheckError").innerHTML="비밀번호가 일치하지 않습니다.";
        objPwd1.focus();
        objPwd2.focus();
        return false;
    } else { document.getElementById("passwordCheckError").innerHTML="";}

    // 학교 선택 안 했을 경우
    if(objUniversity.value == ""){
        document.getElementById("univercityError").innerHTML = "대학교를 선택해주세요";
        objUniversity.focus();
        return false;
    }else{document.getElementById("univercityError").innerHTML = "";}

    //학과 입력 안 했을 경우
    if((objDepartment.value) == ""){
        document.getElementById("departmentError").innerHTML="학과를 입력해주세요";
        objDepartment.focus();
        return false;
    }else{document.getElementById("departmentError").innerHTML="";}



    // //학번을 입력 안 했을 경우
    if(objStudentId.value == ""){
        document.getElementById("studentIdError").innerHTML="학번을 입력해주세요";
        objStudentId.focus();
        return false;
    }else{document.getElementById("studentIdError").innerHTML="";}

    //학번 형식 잘못 입력한 경우
    // if (!check(regul7,objStudentId)) {
    //     document.getElementById("studentIdError").innerHTML="OO학번으로 입력해주세요.";
    //     objStudentId.focus();
    //     return false;
    // } else { document.getElementById("studentIdError").innerHTML=""; }



    // 재학여부 선택 안 했을 경우
    // if(objAttending.value = 'none'){
    //     document.getElementById("attendingError").innerHTML = "재학여부를 선택해주세요";
    //     objAttending.focus();
    //     return false;
    // }else{document.getElementById("attendingError").innerHTML = "";}
    
    //자기소개 제목 입력 안 했을 경우
    // if(objTitle.value == ""){
    //     document.getElementById("titleError").innerHTML="제목을 입력해주세요";
    //     objTitle.focus();
    //     return false;
    // }else{document.getElementById("titleError").innerHTML="";}

    // //자기소개 내용 입력 안 했을 경우
    // if(objDescription.value == ""){
    //     document.getElementById("descriptionError").innerHTML="내용을 입력해주세요";
    //     objDescription.focus();
    //     return false;
    // }else{document.getElementById("descriptionError").innerHTML="";}

 
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