function drawPattern(num){
    var awal = 1
    var tengah = Math.floor(num/2)+1
    var akhir = num
    for (var r=1;r <= num; r++){
        var row = ''

        if (r == tengah){
            for (var m=1;m <= num;m++){
                row = row+' @ '
            }
        }
        else if(r == awal || r == akhir){
            for (var ca=1;ca <= num;ca++){
                if (ca == tengah){
                    row = row+' @ '
                }else{
                    row = row+' = '
                }
            }
        }
        else{
            for (var c=1;c <= num;c++){
                if (c == tengah){
                    row = row+' @ '
                }else{
                    row = row+' = '
                }         
            }
            
        }
        console.log(row+'\n')
    }
}

drawPattern(7)

