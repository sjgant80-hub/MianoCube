# Tutorial 10: Testing & Code OEE

**Industrial-grade quality metrics for your code**

## The Idea

In factories, **OEE** measures equipment health:
- OEE = Availability x Performance x Quality

We apply the SAME formula to code:

| Metric       | Factory              | Code                         |
|-------------|----------------------|------------------------------|
| Availability | Machine uptime       | Modules that import cleanly  |
| Performance  | Running at full rate | Classes with complete APIs   |
| Quality      | Good units produced  | Tests that pass              |

## Running Tests

```bash
# Run all tests with details
pytest tests/ -v

# Run a specific test file
pytest tests/test_core_cube.py -v

# Run tests matching a pattern
pytest tests/ -k "blockarray" -v
```

## Running Code OEE

```bash
python -m tests.run_oee
```

Output looks like:
```
  AVAILABILITY   100.0%  (17/17 modules)   target: >90%
  PERFORMANCE    100.0%  (37/37 contracts)  target: >95%
  QUALITY         98.5%  (65/66 tests)      target: >99%
  ──────────────────────────────────────
  CODE OEE        98.5%  target: >85%

  Grade: WORLD CLASS
```

## Test Templates

Tests are generated dynamically using three templates:

1. **ImportTestTemplate** — discovers all `.py` files,
   generates one import test per module
2. **ModuleTestTemplate** — checks classes expose
   their expected methods and attributes
3. **StateMachineTemplate** — generates valid AND
   invalid transition tests from a state table

## Try It

Add a new method to `Cube` but forget to add a test.
Run OEE. Watch the Performance score drop.
Then add the test and watch it recover.
