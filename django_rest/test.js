const url = 'http://127.0.0.1:8000/api';
async function getdata(){
    try{
        const response = await fetch(url);
        console.log(response)
        const data = await response.json();
        console.log(data)
    }
    catch(error){
        console.log(error);
     
    }

}
const user  ={
    title:'from_script',
    author:'from_rahul_script'
}
const options ={
    method : 'POST',
    body : JSON.stringify(user),
    headers:{
        'Content-Type':'application/json'
    }
}

getdata();
fetch(url,options).then(res => res.json()).then(res => console.log(res));