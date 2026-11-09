import os

files = os.listdir('scratch')
py_files = [f for f in files if f.endswith('.py')]
php_files = [f for f in files if f.endswith('.php')]

print(f"Total Python scripts: {len(py_files)}")
print(f"Total PHP scripts: {len(php_files)}")

# Group scripts by function
verification = [f for f in py_files if 'verify' in f or 'audit' in f]
check_scripts = [f for f in py_files if f.startswith('check_') or f.startswith('inspect_') or f.startswith('find_') or f.startswith('scan_')]
crop_scripts = [f for f in py_files if f.startswith('crop_') or f.startswith('gen_') or f.startswith('generate_')]
test_scripts = [f for f in py_files if f.startswith('test_') or f.startswith('compare_')]
other_py = [f for f in py_files if f not in verification + check_scripts + crop_scripts + test_scripts]

print("\nVerification / Audit scripts:", verification)
print("Check / Inspect scripts count:", len(check_scripts))
print("Crop / Gen scripts count:", len(crop_scripts))
print("Test / Compare scripts count:", len(test_scripts))
print("Other Python scripts count:", len(other_py))

