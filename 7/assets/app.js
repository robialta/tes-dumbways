var app = new Vue({
    el: '#app',
    data: {
      heading_text: 'Selamat datang di aplikasi quick count',
      calons : [
        {'id' : 1,'nama': 'Sulhadi', 'suara' : 100},
        {'id' : 2,'nama': 'Dipo', 'suara' : 123},
        {'id' : 3,'nama': 'Hadi', 'suara' : 90}
    ]
    },
    methods : {
      add(id){
        this.calons.forEach(element => {
          if(element.id == id){
            element.suara+=1
          }
        });
      }
    }

  })