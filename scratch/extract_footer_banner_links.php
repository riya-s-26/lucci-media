<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/tsa.html');
$pos = strpos($html, 'id="footer-banner"');
if ($pos !== false) {
    echo substr($html, $pos + 1800, 2000);
}

