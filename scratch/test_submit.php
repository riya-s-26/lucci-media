<?php
$_SERVER['REQUEST_METHOD'] = 'POST';
$_POST = [
    'name' => 'Sophia Lauren',
    'brand_name' => 'Aura Skin Clinic',
    'website_handle' => 'www.auraskin.com / @auraskin',
    'location' => 'Boston, MA',
    'brand_type' => 'Med spa or clinic',
    'interest' => 'Social media management',
    'monthly_revenue' => '$50K to $100K',
    'marketing_budget' => '$5,000 to $10,000',
    'start_date' => '2027-02-01',
    'success_vision' => 'Expand our client bookings by 40% and establish a cohesive high-fashion visual identity on social.',
    'referral_source' => 'Instagram'
];

require __DIR__ . '/../submit-inquiry.php';
