const dict={"1,1":0,"1,2":0,"1,3":0,"2,1":0,"2,2":0,"2,3":0,"3,1":0,"3,2":0,"3,3":0}
const ans=["1,2","1,3","2,2","2,3"]
function togglePressed(button,num) {
	button.classList.toggle("pressed");
	console.log(num)
	dict[num]++;
}
function same(key,ans){
	for (var a in ans){
		console.log("same func",ans[a],key)
		if(ans[a]==key){
			return true
		}
	}
	return false
}
function enter(){
	var count=0
	for (var key in dict){
		//console.log("key is",key)
		var a=same(key,ans)
		console.log("same func is",a)
		if(dict[key]>0 & dict[key]%2!=0){
			if(a==false){
				count=-1
				break
			}
			count++;
			
		}
	}
	if(count==(ans.length)){
		console.log("おめでとう")
		showCongrats();
	}else{
		console.log("ざんねん")
		var sample = 'あなたは本当に人間ですか？';
		alert(sample);
	}
}
function showCongrats() {
	document.getElementById("congrats-message").style.display = "flex";
}