# CEVA Reference Index

Use this file only as a lightweight navigation index.

- Do not read the whole `reference/` directory by default.
- Prefer loading a single exact file when the request is specific.
- Use `quick-reference.md` or `CEVA_DSP_Intrinsics_Summary.md` only for broad cross-checking.

## Fast Path

If the request already looks like a filename or operation stem, open that exact file first.

- `semi complex 32x16` -> [semi-complex32x16.md](semi-complex32x16.md)
- `semi complex 32x16 with exponent` -> [semi-complex32x16WithExponent.md](semi-complex32x16WithExponent.md)
- `complex 32x16` -> [complex32x16.md](complex32x16.md)
- `vector pack 72 bits` -> [vectorPack72-bits.md](vectorPack72-bits.md)
- `vector shift 72 bit` -> [vectorShift72-bit.md](vectorShift72-bit.md)
- `vector exponent long 72 bit` -> [vectorExponentLong72-bit.md](vectorExponentLong72-bit.md)
- `load predicate` -> [loadPredicate.md](loadPredicate.md)
- `store predicate register` -> [storePredicateRegister.md](storePredicateRegister.md)

## Broad Summaries

- [quick-reference.md](quick-reference.md)
- [CEVA_DSP_Intrinsics_Summary.md](CEVA_DSP_Intrinsics_Summary.md)

## Core Families

### Load And Store

- [load.md](load.md)
- [store.md](store.md)
- [loadPredicate.md](loadPredicate.md)
- [storePredicateRegister.md](storePredicateRegister.md)
- [loadCoefficient.md](loadCoefficient.md)
- [store32BitCoefficient.md](store32BitCoefficient.md)

### Arithmetic And Logic

- [addition.md](addition.md)
- [subtract.md](subtract.md)
- [absolute.md](absolute.md)
- [negate.md](negate.md)
- [round.md](round.md)
- [compare.md](compare.md)
- [predicateRegisterManipulation.md](predicateRegisterManipulation.md)
- [and.md](and.md)
- [or.md](or.md)
- [xor.md](xor.md)

### Shift, Scale, Exponent

- [shift.md](shift.md)
- [scale.md](scale.md)
- [exponent.md](exponent.md)
- [normalize.md](normalize.md)
- [vectorShift.md](vectorShift.md)
- [vectorScale.md](vectorScale.md)
- [vectorExponent32-bit.md](vectorExponent32-bit.md)

### Pack, Unpack, Permute, Transpose

- [pack.md](pack.md)
- [unpack.md](unpack.md)
- [permute.md](permute.md)
- [transpose.md](transpose.md)
- [vectorPack.md](vectorPack.md)
- [vectorUnpack32-bits.md](vectorUnpack32-bits.md)
- [vectorUnpack40-bits.md](vectorUnpack40-bits.md)
- [vectorPermuteWord.md](vectorPermuteWord.md)
- [vectorTransposeWords.md](vectorTransposeWords.md)

### Floating Point And Division

- [floatArithmetic.md](floatArithmetic.md)
- [floatMultiplication.md](floatMultiplication.md)
- [floatDivision.md](floatDivision.md)
- [floatNormalize.md](floatNormalize.md)
- [divide.md](divide.md)
- [squareRoot.md](squareRoot.md)
- [reciprocalSquareRoot.md](reciprocalSquareRoot.md)

### Mode Bits And Configuration

- [automicOperationsModeBits.md](automicOperationsModeBits.md)
- [divisionModeBits.md](divisionModeBits.md)
- [floatingPointModeBits.md](floatingPointModeBits.md)
- [multiplicationModeBits.md](multiplicationModeBits.md)
- [overflowModeBits.md](overflowModeBits.md)
- [roundingModeBits.md](roundingModeBits.md)
- [saturationModeBits.md](saturationModeBits.md)
- [storePre-shiftModeBits.md](storePre-shiftModeBits.md)

## Shape-Based Families

### Scalar And Generic Shapes

- [16x16.md](16x16.md)
- [32x16.md](32x16.md)
- [32x32.md](32x32.md)
- [16x16WithExponent.md](16x16WithExponent.md)
- [32x16WithExponent.md](32x16WithExponent.md)
- [32x32Mac3.md](32x32Mac3.md)

### Complex Shapes

- [complex16x16.md](complex16x16.md)
- [complex32x16.md](complex32x16.md)
- [complex32x32.md](complex32x32.md)
- [complex16x16WithExponent.md](complex16x16WithExponent.md)
- [complex32x16WithExponent.md](complex32x16WithExponent.md)

### Semi-Complex Shapes

- [semi-complex16x16.md](semi-complex16x16.md)
- [semi-complex16x32.md](semi-complex16x32.md)
- [semi-complex32x16.md](semi-complex32x16.md)
- [semi-complex32x32.md](semi-complex32x32.md)
- [semi-complex16x16WithExponent.md](semi-complex16x16WithExponent.md)
- [semi-complex16x32WithExponent.md](semi-complex16x32WithExponent.md)
- [semi-complex32x16WithExponent.md](semi-complex32x16WithExponent.md)

### Vector Variants

- [vectorComplex.md](vectorComplex.md)
- [vectorCompare.md](vectorCompare.md)
- [vectorPack.md](vectorPack.md)
- [vectorShift.md](vectorShift.md)
- [vectorScale.md](vectorScale.md)
- [vectorFloatingPointDivision.md](vectorFloatingPointDivision.md)

## Width-Specific Files

Prefer these over generic files when the request explicitly mentions bit width.

### 40-Bit

- [vectorShift40-bit.md](vectorShift40-bit.md)
- [vectorExponent40-bit.md](vectorExponent40-bit.md)
- [vectorUnpack40-bits.md](vectorUnpack40-bits.md)

### 64-Bit

- [vectorAdd64-bit.md](vectorAdd64-bit.md)
- [vectorSubtract64-bit.md](vectorSubtract64-bit.md)
- [vectorExponentLong64-bit.md](vectorExponentLong64-bit.md)
- [vectorPack64-bits.md](vectorPack64-bits.md)

### 72-Bit

- [vectorAdd72-bit.md](vectorAdd72-bit.md)
- [vectorSubtract72-bit.md](vectorSubtract72-bit.md)
- [vectorShift72-bit.md](vectorShift72-bit.md)
- [vectorExponentLong72-bit.md](vectorExponentLong72-bit.md)
- [vectorPack72-bits.md](vectorPack72-bits.md)

## Special-Purpose Files

- [demapper.md](demapper.md)
- [vectorDemapper.md](vectorDemapper.md)
- [hermitianMatrixDeterminant.md](hermitianMatrixDeterminant.md)
- [traceback.md](traceback.md)
- [vectorTraceback.md](vectorTraceback.md)

## Notes

- This index is intentionally selective and de-duplicated.
- If a request names a more specific file than the ones listed here, prefer that exact file.
- If a request is broad, start from a summary file, then narrow to one or two exact reference files.

