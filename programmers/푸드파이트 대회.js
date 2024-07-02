function solution(food) {
    var answer = '';
    
    for(let i=1;i<food.length;i++){
        // 앞 절반 추가
        for(let j=0;j<Math.floor(food[i]/2);j++){
            answer += i
        }

    }

    // 뒤 절반 추가
    back = answer.split("").reverse().join("");
    answer = answer + '0' + back;
    
    return answer;
}