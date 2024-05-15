Object.defineProperty(Date.prototype,"format",{
    enumerable:false,
    value:function(mask){
        return mask
        .replace(/dd/g,this.getDate()+1<10 ?"0"+(this.getDate()+1):this.getDate()+1 )
        .replace(/mm/g,this.getMonth()+1<10?"0"+(this.getMonth()+1):this.getMonth()+1)
        .replace(/yyyy/g,this.getFullYear()<10?"0"+this.getFullYear():this.getFullYear())
        .replace(/yy/g,this.getFullYear()-100);
    }
});

console.log('123');