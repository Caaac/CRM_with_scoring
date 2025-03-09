Object.defineProperty(Object.prototype, "toHumanDate", {
  enumerable: false,
  value: function() {
    return new Intl.DateTimeFormat("ru", {dateStyle: "long"}).format(new Date(this))
  },
});

Object.defineProperty(Date.prototype, "toISOFullDate", {
  enumerable: false,
  value: function() {
      return (
          this.getFullYear() +
          "-" +
          (this.getMonth() + 1).toString().padStart(2, "0") +
          "-" +
          this.getDate()
              .toString()
              .padStart(2, "0")
      );
  },
});

Object.defineProperty(Object.prototype,"toMonetarily",{
  enumerable:false,
  value:function(){
       const number = parseFloat(String(this).replace(/[^\d.,-]/g, '').replace(',', '.')) || 0;
       return number.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$& ').replace('.', ',') + ' ₽';
  }
});

Object.defineProperty(Object.prototype,"toPersent",{
  enumerable:false,
  value:function(){
       const number = parseFloat(String(this).replace(/[^\d.,]/g, '').replace(',', '.')) || 0;
       return number.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$& ').replace('.', ',') + ' %';
  }
});

Object.defineProperty(Object.prototype,"toHourly",{
  enumerable:false,
  value:function(){
       const number = parseFloat(String(this).replace(/[^\d.,]/g, '').replace(',', '.')) || 0;
       return number.toFixed(1).replace(/\d(?=(\d{3})+\.)/g, '$& ').replace('.', ',') + ' ч';
  }
});

Object.defineProperty(Date.prototype, "toMonthFullDate", {
  enumerable: false,
  value: function() {
      return (
          this.getDate()
          .toString() +
          " " +
          this.toLocaleString('default', { month: 'long' }) +
          " " +
          this.getFullYear()
      );
  },
});

Object.defineProperty(Object.prototype, 'deepCopy', {
  enumerable: false,
  value: function () {
    return JSON.parse(JSON.stringify(this))
  }
})