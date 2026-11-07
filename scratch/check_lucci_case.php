<?php
$h = file_get_contents('scratch/luccimedia.html');
preg_match_all('/<h[1-6][^>]*>(.*?)<\/h[1-6]>/is', $h, $m);
foreach (array_slice($m[1], 0, 10) as $t) {
    echo trim(strip_tags($t)) . "\n---\n";
}

