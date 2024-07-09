function solution(n, m) {
    let max = 1;
    let min = Math.max(n, m);
    
    for(let i=1;i<=Math.max(n,m);i++) {
        if(n%i==0 && m%i==0) {
            max = i;
        }                
    }
    
    for(let i=1;i<=n*m;i++) {
        if(i%n==0&&i%m==0){
            min = i;
            break;
        }
    }
    
    return [max, min];
}