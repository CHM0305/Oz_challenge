//제출이벤트 받기(이벤트 핸들링)
const form = document.getElementById("form")

form.addEventListener("submit",function(event){
    event.preventDefault()//기존 기능 차단

    let userId= event.target.id.value
    let userPw1= event.target.pw1.value
    let userPw2= event.target.pw2.value
    let userName= event.target.name.value
    let userPhone= event.target.phone.value
    let userPosition= event.target.position.value
    let userGender= event.target.gender.value
    let userEmail= event.target.email.value
    let userIntro= event.target.intro.value

    //console.log(userId,userPw1,userPw2,userName,userPhone,userPosition,
    //    userGender,userEmail,userIntro)

    if(userId.length<6){
        alert("아이디가 짧습니다. 다시 입력해주세요.")
        return
    }
    if(userPw1 !== userPw2){
        alert("비밀번호가 일치하지 않습니다.")
        return
    }


    //가입이 성공적으로 완료!!
    document.body.innerHTML = ""

    document.write(`<h1> ${userId}님 환영합니다 </h1>`)
    document.write(`<h3> 회원 가입 시 입력하시 내역은 다음과 같습니다. </h3>`)
    document.write(`<p> 아이디 : ${userId}</p>`)
    document.write(`<p> 이름 : ${userName} </p>`)
    document.write(`<p> 전화번호 : ${userPhone} </p>`)
    document.write(`<p> 직무 : ${userPosition} </p>`)

})
//제출된 입력 값들을 참조
//입력 값에 문제가 있는 경우 이를 감지
//가입 환영 인사를 제공