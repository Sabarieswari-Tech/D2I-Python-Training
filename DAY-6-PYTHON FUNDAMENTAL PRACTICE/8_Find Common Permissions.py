permissions = {
    'admin': {'read', 'write', 'delete'},
    'operator': {'read', 'write'},
    'auditor': {'read', 'export'}
}

sets = list(permissions.values())

common = sets[0]
all_permissions = sets[0]

for s in sets[1:]:
    common = common & s
    all_permissions = all_permissions | s

print("Common permissions:", sorted(common))
print("All permissions:", sorted(all_permissions))