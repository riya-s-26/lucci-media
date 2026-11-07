<?php
$lines = file('c:/xampp/htdocs/luci/scratch/lucci_copy.txt');
$headlines = [];
foreach ($lines as $l) {
    $l = trim($l);
    if (strpos($l, '{') === false && strpos($l, '}') === false && strpos($l, ';') === false && strpos($l, '<') === false && strpos($l, '=') === false && strpos($l, '(') === false && !preg_match('/^[0-9\s\.\,\-]+$/', $l)) {
        if (strlen($l) > 15 && strlen($l) < 120) {
            $headlines[] = $l;
        }
    }
}
$headlines = array_unique($headlines);
echo "Headlines found: " . count($headlines) . "\n";
foreach (array_slice($headlines, 0, 40) as $h) {
    echo "• " . $h . "\n";
}

