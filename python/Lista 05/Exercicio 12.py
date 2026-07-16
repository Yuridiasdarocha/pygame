totalaptos = 75
diarianormal = 292
diariapromocional = diarianormal * 0.25
arrecadacaopromo = (totalaptos * 0.80) * diariapromocional
arrecadacaonormal = (totalaptos * 0.50) * diarianormal
diferenca = arrecadacaopromo - arrecadacaonormal
print (f"O valor da diária promocional: R${diariapromocional}")
print (f"O valor total arrecadado com 80% de ocupação e diária promocional: R${arrecadacaopromo}")
print (f"O valor da arrecadação normal com 50% de ocupação: R${arrecadacaonormal}")
print (f"Diferença: {diferenca}")
