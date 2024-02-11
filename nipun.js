input = {
  Signature : "abc",
  Command : "purchase",
  Amount : "abc"
}

temp = []
for(let value in input){
  temp.push(value + "=" + input[value]);
}
temp.sort()
res = ""
temp.forEach(element => {
  res += element
});

console.log(res);
