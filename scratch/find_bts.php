<?php
$html = file_get_contents('c:/xampp/htdocs/luci/scratch/luccimedia.html');
$pos = strpos($html, 'BEHIND THE SCENES');
if ($pos !== false) {
    echo substr($html, $pos - 300, 2000);
} else {
    echo "not found";
}

