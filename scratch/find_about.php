<?php
$c = file_get_contents('c:/xampp/htdocs/luci/scratch_tsa.html');
preg_match_all('/\.sie-intro-banner[^{]*\{[^}]*\}/', $c, $m);
foreach ($m[0] as $rule) {
    echo $rule . "\n";
}
