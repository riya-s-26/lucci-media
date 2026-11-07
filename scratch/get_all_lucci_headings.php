<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
preg_match_all('/<h[1-4][^>]*>(.*?)<\/h[1-4]>/is', $html, $headings);
foreach ($headings[1] as $h) {
    $clean = trim(strip_tags($h));
    if (!empty($clean)) {
        echo "• $clean\n";
    }
}

