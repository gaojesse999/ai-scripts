# CEVA DSP Intrinsics Quick Reference

A cheat sheet of the most commonly used CEVA DSP intrinsics in L1SW.

## Most Common Intrinsics

### Memory Operations (Load/Store)

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vlddw_v32(mdw, src, dest, offset)` | Load 32-bit vector | `_vlddw_v32(mdw_8dw, in, vData, 0)` |
| `_vstdw_v32(mdw, src, offset, dest)` | Store 32-bit vector | `_vstdw_v32(mdw_8dw, vOut, 0, out)` |
| `_vlddw_c32_clone_1dw(src, dest)` | Broadcast scalar | `_vlddw_c32_clone_1dw(&val, vVal)` |
| `_vlddw_pm_imm_v32(mdw, src, dest, step, off)` | Load with post-increment | `_vlddw_pm_imm_v32(mdw_8dw, ptr, vD, 32, 0)` |

### Arithmetic

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vadd_v32(a, b, out)` | Vector add | `_vadd_v32(vA, vB, vSum)` |
| `_vadd_s_v32(a, b, out)` | Vector add (saturate) | `_vadd_s_v32(vA, vB, vSum)` |
| `_vsub_v32(a, b, out)` | Vector subtract | `_vsub_v32(vA, vB, vDiff)` |
| `_vabs_v32(in, out)` | Absolute value | `_vabs_v32(vData, vAbs)` |
| `_vneg_v32(in, out)` | Negate | `_vneg_v32(vData, vNeg)` |
| `_vmax_v32(a, b, out)` | Element-wise max | `_vmax_v32(vA, vB, vMax)` |
| `_vmin_v32(a, b, out)` | Element-wise min | `_vmin_v32(vA, vB, vMin)` |

### Multiply & MAC

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vmul_v32(a, b, out)` | Vector multiply | `_vmul_v32(vA, vB, vProd)` |
| `_vmac_v40(a, b, acc)` | MAC: acc += a*b | `_vmac_v40(vA, vB, vAcc)` |
| `_vcmul_v32(a, b, out)` | Complex multiply | `_vcmul_v32(vSig, vCoeff, vOut)` |
| `_vcmac_v40(a, b, acc)` | Complex MAC | `_vcmac_v40(vA, vB, vAcc)` |
| `_vcmulcj_v32(a, b, out)` | Complex mul (conj) | `_vcmulcj_v32(vA, vB, vOut)` |
| `_vcmaccj_v40(a, b, acc)` | Complex MAC (conj) | `_vcmaccj_v40(vSig, vRef, vAcc)` |

### Shift & Round

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vlsl_v32(in, shift, out)` | Left shift | `_vlsl_v32(vData, 4, vShift)` |
| `_vasr_v32(in, shift, out)` | Arithmetic right shift | `_vasr_v32(vData, 8, vShift)` |
| `_vrnd_asr_v40(in, shift, out)` | Round & right shift | `_vrnd_asr_v40(vAcc, 15, vOut)` |

### Comparison & Logical

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vcmpgt_v32(a, b, vpr)` | Compare greater than | `_vcmpgt_v32(vA, vB, vpr0)` |
| `_vcmpeq_v32(a, b, vpr)` | Compare equal | `_vcmpeq_v32(vA, vB, vpr0)` |
| `_vand_v32(a, b, out)` | Bitwise AND | `_vand_v32(vData, vMask, vOut)` |
| `_vor_v32(a, b, out)` | Bitwise OR | `_vor_v32(vA, vB, vOut)` |
| `_vsel_v32(cond, a, b, out)` | Select: cond?a:b | `_vsel_v32(vpr0, vA, vB, vOut)` |

### Pack/Unpack

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vpack_v40_v32(in40, out32)` | Pack 40→32 (saturate) | `_vpack_v40_v32(vAcc, vOut)` |
| `_vunpck_v32_v40(in32, out40)` | Unpack 32→40 | `_vunpck_v32_v40(vData, vData40)` |
| `_vitlv_v32(a, b, out)` | Interleave | `_vitlv_v32(vI, vQ, vIQ)` |

### Initialization

| Intrinsic | Purpose | Example |
|-----------|---------|---------|
| `_vcu_declaration()` | Declare VCU usage | `_vcu_declaration();` |
| `_vclr_v32(out)` | Clear to zero | `_vclr_v32(vZero)` |
| `_vfill_v32(val, out)` | Fill with value | `_vfill_v32(0x1000, vConst)` |

## Naming Convention Guide

### Prefixes
- `_v`: Vector operation
- `_vl`: Vector load
- `_vs`: Vector store
- `_vc`: Vector complex operation

### Suffixes
- `_v32`: 32-bit vector data
- `_v40`: 40-bit vector data (extended precision)
- `_s`: Saturating arithmetic
- `_p`: Predicated (conditional using VPR)
- `_pm`: Post-modification (auto-increment)
- `_imm`: Immediate operand
- `_vuX`: VCU-specific (VCU0/VCU1)
- `cj`: Conjugate operation
- `dw`: Double-word (8 bytes)

### MDW (Multi-Double-Word) Sizes
- `mdw_1dw`: 1 × 8 bytes = 8 bytes (2 × 32-bit)
- `mdw_2dw`: 2 × 8 bytes = 16 bytes (4 × 32-bit)
- `mdw_4dw`: 4 × 8 bytes = 32 bytes (8 × 32-bit)
- `mdw_8dw`: 8 × 8 bytes = 64 bytes (16 × 32-bit)

## Common Patterns

### Pattern 1: Basic Vector Processing Loop
```c
_vcu_declaration();
__vu32 vIn, vOut;

for (int i = 0; i < count; i += 8) {
    _vlddw_v32(mdw_8dw, &input[i], vIn, 0);
    // Process vIn -> vOut
    _vstdw_v32(mdw_8dw, vOut, 0, &output[i]);
}
```

### Pattern 2: MAC Accumulation
```c
_vcu_declaration();
__vu32 vA, vB;
__vu40 vAcc;

_vclr_v40(vAcc);
for (int i = 0; i < N; i += 8) {
    _vlddw_v32(mdw_8dw, &a[i], vA, 0);
    _vlddw_v32(mdw_8dw, &b[i], vB, 0);
    _vmac_v40(vA, vB, vAcc);  // acc += a * b
}
```

### Pattern 3: Scaling with Fixed-Point
```c
// Scale by factor (Q15 format)
_vmul_v32(vData, vScale, vProd40);       // 32-bit × 32-bit = 40-bit
_vrnd_asr_v40(vProd40, 15, vScaled);     // Shift right 15 bits with rounding
```

### Pattern 4: Conditional Processing
```c
__vpr vpr0;

// Generate condition mask
_vcmpgt_v32(vData, vThreshold, vpr0);

// Conditional operation (only where vpr0 is true)
_vadd_p_v32(vpr0, vData, vDelta, vResult);
```

### Pattern 5: Post-Modified Loop
```c
int step = 32;  // Step in bytes for mdw_8dw
int8_t* ptr = input;

for (int i = 0; i < count; i += 8) {
    // Load with post-increment
    _vlddw_pm_imm_v32(mdw_8dw, ptr, vData, step, 0);
    // ptr automatically increments by step
}
```

### Pattern 6: Complex Correlation
```c
__vu32 vSig, vRef;
__vu40 vCorr;

_vclr_v40(vCorr);
for (int i = 0; i < N; i += 8) {
    _vlddw_v32(mdw_8dw, &signal[i], vSig, 0);
    _vlddw_v32(mdw_8dw, &reference[i], vRef, 0);
    _vcmaccj_v40(vSig, vRef, vCorr);  // corr += sig * conj(ref)
}
```

## Q-Format Reference

| Format | Range | Resolution | Usage |
|--------|-------|------------|-------|
| Q15 (16-bit) | -1.0 to ~0.999969 | 1/32768 | Coefficients, normalized data |
| Q31 (32-bit) | -1.0 to ~0.9999999995 | 1/2147483648 | High precision coefficients |
| Q0.15 | Same as Q15 | | Alternative notation |
| Q15.16 (32-bit) | -32768 to 32767.99998 | 1/65536 | Large range with fractional |

### Scaling Rules
- **Multiply**: Q_a × Q_b = Q_(a+b) → Need to shift right by 'a' or 'b'
- **Add/Sub**: Q_a + Q_a = Q_a (no shift needed)
- **Division**: Shift dividend left by 'b' before dividing for Q_b result

## Performance Tips

1. **Alignment**: Ensure 32-byte alignment for `mdw_8dw` operations
2. **MDW size**: Use largest MDW that fits your data (prefer `mdw_8dw`)
3. **Post-modification**: Reduces address calculation overhead
4. **Dual VCU**: Process two independent streams in parallel
5. **Predication**: Faster than branches for conditional operations
6. **MAC over MUL+ADD**: Single instruction, better throughput
7. **Saturating arithmetic**: Prevents overflow without branches

## Common Mistakes to Avoid

❌ **Wrong MDW size**: `_vlddw_v32(mdw_1dw, ...)` when you need 8 elements  
✅ **Correct**: `_vlddw_v32(mdw_8dw, ...)` for 8 × 32-bit = 256 bits

❌ **Forgetting saturation**: `_vadd_v32()` can overflow  
✅ **Use**: `_vadd_s_v32()` for robust arithmetic

❌ **Ignoring alignment**: Unaligned loads/stores are slower  
✅ **Align data**: `__attribute__((aligned(32)))` for vectors

❌ **Wrong Q-format shift**: `_vmul_v32()` then forget to shift  
✅ **Round & shift**: `_vrnd_asr_v40(vProd, 15, vOut)` for Q15×Q15

❌ **Mixing VCU0/VCU1 incorrectly**: Cross-VCU dependencies stall  
✅ **Independent streams**: Keep VCU0 and VCU1 processing separate

## Quick Lookup by Use Case

| Need | Use This Intrinsic |
|------|-------------------|
| Load 8 × 32-bit values | `_vlddw_v32(mdw_8dw, ...)` |
| Store 8 × 32-bit values | `_vstdw_v32(mdw_8dw, ...)` |
| Broadcast constant | `_vlddw_c32_clone_1dw(&const, v)` |
| Add with overflow protection | `_vadd_s_v32(...)` |
| Dot product | `_vmac_v40()` in loop |
| Complex multiply | `_vcmul_v32()` or `_vcmac_v40()` |
| Correlation | `_vcmaccj_v40()` (MAC with conjugate) |
| Scale Q15 data | `_vmul_v32()` + `_vrnd_asr_v40()` |
| Find maximum | `_vmax_v32()` |
| Zero initialize | `_vclr_v32()` |
| Conditional operation | `_vcmpXX()` + `_v*_p_*()` |
| Pack 40-bit to 32-bit | `_vpack_v40_v32()` |

---

For detailed documentation, see:
- **Full intrinsics reference**: Other files in `intrinsics-reference/` folder
- **Main CEVA DSP skill**: [SKILL.md](../SKILL.md)
- **L1SW intrinsics catalog**: `/var/work/mtx678/project/l1sw/CEVA_DSP_Intrinsics_Summary.md`
