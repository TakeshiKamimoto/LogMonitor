<?php

//データーベースに接続
$con = mysql_connect('localhost', 'USER', 'PASSWORD');
mysql_select_db('DATABASE_NAME');

//温度湿度計コマンド実行
exec( '/usr/local/bin/usbrh',$buf);
list($temp , $hum ) = explode(" ",$buf[0]);

//不快指数の計算 http://homepage2.nifty.com/luminaries/guidance/kishou_018.htm
//０．８１×気温＋０．０１×湿度×（０．９９×気温－１４．３）＋４６．３
$discomfort = 0.81 * $temp + 0.01*$hum*(0.99*$temp-14.3)+46.3;

//Raspberry Piの場合は下記コマンドでCPU温度が取得できます。
exec( '/opt/vc/bin/vcgencmd  measure_temp',$buf2);
list($str , $temp_cpu ) = explode("=",$buf2[0]);
$temp_cpu = floatval( $temp_cpu );

//データーベースへデーターを挿入（変数のmysql_real_escape_stringは適宜してください ）
$sql = <<<SQL
INSERT INTO
  temperature_data (
    temperature,
    humidity,
    discomfort,
    temperature_cpu,
    mdatetime
  )VALUES(
    '{$temp}',
    '{$hum}',
    '{$discomfort}',
    '{$temp_cpu}',
    NOW()
  );
SQL;
$res = mysql_query( $sql );
