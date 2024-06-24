function solution(name, yearning, photo) {
    var answer = [];
    
    photo.forEach((e) => {
        let tmp = 0
        for(let n of e) {
            let check = yearning[name.indexOf(n)];            
            
            if (check !== undefined) {
                tmp += check
            }
        }

        answer.push(tmp)
    })
        
    
    return answer;
}