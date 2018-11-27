instruction=['mov','add','sub','call','inc','dec','push','pop','not','and','or','xor','jmp','je','jne','jg','jng','jge','jnge','jl','jnl','jle','jnle','jz','jnz','loop','fstp','fld','cmp','ret']
instruction_symbol=['MOVSB','MOVSW','MOVSD','STOSB','STOSW','STOSD','LODSB','LODSW','LODSD','SCASB','SACSW','SACSD','CMPSB','CMPSW','CMPSD','CLD','STD','REP','REPE','REPNE','REPZ','REPNZ']
label_set=['jmp','je','jne','jg','jng','jge','jnge','jl','jnl','jle','jnle','jz','jnz','call']

literal_instr=['mov','add','sub','cmp','push','pop','fstp','fld']

data={'dw':2,'dd':4,'dq':8,'dt':10}
bss={'resb':1,'resw':2,'resd':4,'resq':8,'rest':10}
