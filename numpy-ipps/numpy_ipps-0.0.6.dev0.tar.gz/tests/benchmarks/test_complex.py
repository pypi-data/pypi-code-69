import importlib
import logging
import os

import numpy
import pytest

import numpy_ipps
import numpy_ipps.policies


cache_L1 = numpy.min(
    [cache_size for _u0, _u1, cache_size in numpy_ipps.support.cache_params()]
)
orders = (
    8,
    int(numpy.ceil(numpy.log2(cache_L1))),
)
dtypes = (
    numpy.complex64,
    numpy.complex128,
)
if (
    "NUMPY_IPPS_FAST_TEST" in os.environ
    and os.environ["NUMPY_IPPS_FAST_TEST"] == "ON"
):
    dtypes = (numpy.complex64,)


binary_classes = (
    numpy_ipps.MulByConj,
    numpy_ipps.MulByConjFlip,
)

unary_classes = (
    numpy_ipps.Conj,
    numpy_ipps.ConjFlip,
)
unaryFC_classes = (
    numpy_ipps.Modulus,
    numpy_ipps.Arg,
    numpy_ipps.Real,
    numpy_ipps.Imag,
)
unaryI_classes = (
    numpy_ipps.Conj_I,
    numpy_ipps.ConjFlip_I,
)


@pytest.fixture(scope="module")
def logger_fixture(pytestconfig):
    logger = logging.getLogger("numpy_ipps")
    logger.setLevel(logging.DEBUG)

    log_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "log_ref",
        "test_complex.log",
    )
    ch = logging.FileHandler(log_file, mode="w")
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter("%(message)s"))

    logger.addHandler(ch)
    importlib.reload(numpy_ipps)

    yield logger

    logger.removeHandler(ch)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", binary_classes)
def test_ipps_binary(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src1 = (1 + numpy.random.rand(1 << order)).astype(dtype)
    src2 = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=dtype)
    dst_ref = numpy.empty(1 << order, dtype=dtype)

    with numpy_ipps.utils.context(src1, src2, dst, dst_ref):
        benchmark(feature_obj, src1, src2, dst)
        feature_obj._numpy_backend(src1, src2, dst_ref)

    numpy.testing.assert_array_almost_equal_nulp(dst, dst_ref, nulp=5)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", binary_classes)
def test_numpy_binary(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src1 = (1 + numpy.random.rand(1 << order)).astype(dtype)
    src2 = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=dtype)

    with numpy_ipps.utils.context(src1, src2, dst):
        benchmark(feature_obj._numpy_backend, src1, src2, dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unary_classes)
def test_ipps_unary(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=dtype)
    dst_ref = numpy.empty(1 << order, dtype=dtype)

    with numpy_ipps.utils.context(src, dst, dst_ref):
        benchmark(feature_obj, src, dst)
        feature_obj._numpy_backend(src, dst_ref)

    numpy.testing.assert_array_almost_equal_nulp(dst, dst_ref, nulp=5)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unaryFC_classes)
def test_ipps_unaryFC(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=src[0].real.dtype)
    dst_ref = numpy.empty(1 << order, dtype=src[0].real.dtype)

    with numpy_ipps.utils.context(src, dst, dst_ref):
        benchmark(feature_obj, src, dst)
        feature_obj._numpy_backend(src, dst_ref)

    numpy.testing.assert_array_almost_equal_nulp(dst, dst_ref, nulp=5)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unaryI_classes)
def test_ipps_unaryI(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src_dst = (1 + numpy.random.rand(1 << order)).astype(dtype)

    with numpy_ipps.utils.context(src_dst):
        benchmark(feature_obj, src_dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unary_classes)
def test_numpy_unary(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=dtype)

    with numpy_ipps.utils.context(src, dst):
        benchmark(feature_obj._numpy_backend, src, dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unaryFC_classes)
def test_numpy_unaryFC(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)
    dst = numpy.empty(1 << order, dtype=src[0].real.dtype)
    dst_ref = numpy.empty(1 << order, dtype=src[0].real.dtype)

    with numpy_ipps.utils.context(src, dst, dst_ref):
        benchmark(feature_obj._numpy_backend, src, dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
@pytest.mark.parametrize("feature", unaryI_classes)
def test_numpy_unaryI(logger_fixture, benchmark, order, dtype, feature):
    if dtype not in feature._ipps_candidates:
        return

    feature_obj = feature(size=1 << order, dtype=dtype)
    src_dst = (1 + numpy.random.rand(1 << order)).astype(dtype)

    with numpy_ipps.utils.context(src_dst):
        benchmark(feature_obj._numpy_backend, src_dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
def test_ipps_RealToCplx(logger_fixture, benchmark, order, dtype):
    dst = numpy.empty(1 << order, dtype=dtype)
    dst_ref = numpy.empty(1 << order, dtype=dtype)

    if dtype not in numpy_ipps.policies.complex_candidates:
        return

    feature_dtype = dst[0].real.dtype
    feature_obj = numpy_ipps.RealToCplx(size=1 << order, dtype=feature_dtype)
    src_re = (1 + numpy.random.rand(1 << order)).astype(feature_dtype)
    src_im = (1 + numpy.random.rand(1 << order)).astype(feature_dtype)

    with numpy_ipps.utils.context(src_re, src_im, dst, dst_ref):
        benchmark(feature_obj, src_re, src_im, dst)
        feature_obj._numpy_backend(src_re, src_im, dst_ref)

    numpy.testing.assert_array_almost_equal_nulp(dst, dst_ref, nulp=5)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
def test_numpy_RealToCplx(logger_fixture, benchmark, order, dtype):
    dst = numpy.empty(1 << order, dtype=dtype)

    if dtype not in numpy_ipps.policies.complex_candidates:
        return

    feature_dtype = dst[0].real.dtype
    feature_obj = numpy_ipps.RealToCplx(size=1 << order, dtype=feature_dtype)
    src_re = (1 + numpy.random.rand(1 << order)).astype(feature_dtype)
    src_im = (1 + numpy.random.rand(1 << order)).astype(feature_dtype)

    with numpy_ipps.utils.context(src_re, src_im, dst):
        benchmark(feature_obj._numpy_backend, src_re, src_im, dst)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
def test_ipps_CplxToReal(logger_fixture, benchmark, order, dtype):
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)

    if dtype not in numpy_ipps.policies.complex_candidates:
        return

    feature_dtype = src[0].real.dtype
    feature_obj = numpy_ipps.CplxToReal(size=1 << order, dtype=dtype)
    dst_re = numpy.empty(1 << order, dtype=feature_dtype)
    dst_im = numpy.empty(1 << order, dtype=feature_dtype)
    dst_ref_re = numpy.empty(1 << order, dtype=feature_dtype)
    dst_ref_im = numpy.empty(1 << order, dtype=feature_dtype)

    with numpy_ipps.utils.context(src, dst_re, dst_im, dst_ref_re, dst_ref_im):
        benchmark(feature_obj, src, dst_re, dst_im)
        feature_obj._numpy_backend(src, dst_ref_re, dst_ref_im)

    numpy.testing.assert_array_almost_equal_nulp(dst_re, dst_ref_re, nulp=5)
    numpy.testing.assert_array_almost_equal_nulp(dst_im, dst_ref_im, nulp=5)


@pytest.mark.parametrize("order", orders)
@pytest.mark.parametrize("dtype", dtypes)
def test_numpy_CplxToReal(logger_fixture, benchmark, order, dtype):
    src = (1 + numpy.random.rand(1 << order)).astype(dtype)

    if dtype not in numpy_ipps.policies.complex_candidates:
        return

    feature_dtype = src[0].real.dtype
    feature_obj = numpy_ipps.CplxToReal(size=1 << order, dtype=dtype)
    dst_re = numpy.empty(1 << order, dtype=feature_dtype)
    dst_im = numpy.empty(1 << order, dtype=feature_dtype)

    with numpy_ipps.utils.context(src, dst_re, dst_im):
        benchmark(feature_obj._numpy_backend, src, dst_re, dst_im)
