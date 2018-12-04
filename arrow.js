{

const func = (x,y) => { 　　　//アロー関数という。
    const answer = x + y;
    return answer;
};
console.log(func(3,5));
}


{

const func = (x,y) => {return x + y; }; //戻り値を省略して書ける
console.log(func(5,2));
}


const func = (x,y) => {return x + y}; // return文を明示しないと文たちの値を返せない。
console.log(func(2,4));

