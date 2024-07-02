function solution(s) {
    var answer = [];
    var map = {};
    
    for(let i=0;i<s.length;i++){
        if(map.hasOwnProperty(s[i])){
            answer.push(i-map[s[i]]);
            map[s[i]] = i;
        }else{
            map[s[i]] = i;
            answer.push(-1);
        }
    }
    
    return answer;
}