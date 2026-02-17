# 📐 KONOMI STANDARD 📐

**Self-Defining Industrial Standards Compression v1.0**

## 🧬 LAYER 0: META-STANDARD

How standards are defined — the standard that defines standards.

```
STD = {
  id: str,              # unique key (ISA-95, ISA-88, etc)
  scope: str,           # what it covers
  udt: [UDT],           # user defined types FIRST
  hierarchy: [LEVEL],   # levels/layers if applicable
  states: [STATE_MACHINE],
  entities: [ENTITY],
  relations: [RELATION],
  rules: [RULE],
  crosswalk: {std_id: MAP}
}
```

```
UDT = {
  name: str,
  base: str|null,       # inherits from
  fields: [{name, type, unit, range, desc}],
  methods: [{name, params, returns, desc}],
  constraints: [RULE]
}
```

```
LEVEL = {
  id: int|str,
  name: str,
  scope: str,
  timescale: str,
  systems: [str],
  data_down: [str],
  data_up: [str]
}
```

```
STATE_MACHINE = {
  name: str,
  states: [str],
  initial: str,
  transitions: [{from, to, trigger, guard, action}]
}
```

```
ENTITY = {
  name: str,
  udt: str,
  parent: str|null,
  children: [str],
  tags: {category: [TAG_DEF]}
}
```

```
RELATION = {
  type: contains|references|triggers|produces|consumes,
  from: str, to: str,
  cardinality: 1:1|1:N|N:M
}
```

```
RULE = {
  id: str,
  condition: expr,
  action: str,
  severity: info|warn|error|fatal
}
```

```
CROSSWALK = {
  from_std: str, from_entity: str,
  to_std: str, to_entity: str,
  mapping: exact|partial|semantic,
  transform: expr|null
}
```

## 🔷 LAYER 1: BASE UDTs

Primitives all standards use.

### Identifier Types

| Name | Type | Scope        | Format                     |
|------|------|--------------|----------------------------|
| UUID | str  | global       | xxxxxxxx-xxxx-xxxx-...     |
| PATH | str  | hierarchical | A/B/C/D                    |
| TAG  | str  | equipment    | Area_Unit_Module_Point     |
| URN  | str  | global       | urn:domain:type:id         |

### Timestamp, Quality, Value

- **ISO8601**: ms resolution, UTC
- **Quality**: GOOD=192, BAD=0, UNCERTAIN=64
- **Value**: {v, q, t, unit}
- **Range**: {lo, hi, lo_inc, hi_inc, unit}
- **Quantity**: {value, unit, uncertainty}

## 🏗️ LAYER 2: ISA-95

Enterprise↔Control Integration.

**Levels**: L4 Business → L3 MOM → L2 Control → L1 Sensing → L0 Process

**Hierarchy**: Enterprise → Site → Area → WorkCenter → WorkUnit → Equipment

**Key UDTs**: Equipment, Material, Personnel, ProcessSegment,
ProductionSchedule, ProductionPerformance

## 🧪 LAYER 3: ISA-88

Batch Process Control.

**Equipment**: ProcessCell → Unit → EquipmentModule → ControlModule

**Recipes**: GeneralRecipe → SiteRecipe → MasterRecipe → ControlRecipe

**Procedure**: Procedure → UnitProcedure → Operation → Phase

**Phase States**: IDLE→RUNNING→COMPLETE (with HOLD/STOP/ABORT branches)

## 🖥️ LAYER 4: ISA-101

HMI Design. Situational awareness > aesthetics.

**Layers**: L1 Overview → L2 Area → L3 Unit → L4 Detail → L5 Support

**Color = Meaning**: Gray=Normal, Green=Running, Red=Alarm,
Yellow=Warning, Blue=Maintenance, Orange=Manual

## 🚨 LAYER 5: ISA-18.2

Alarm Management Lifecycle.

**Priority**: P1 Emergency (<1min) → P4 Low (shift)

**States**: NORMAL → UNACK → ACKED → NORMAL

**Target**: <6 alarms/hr avg, <12 peak

## 📡 LAYER 6: OPC-UA

Industrial interoperability. Nodes, variables, methods, subscriptions.

## 📨 LAYER 7: MQTT/Sparkplug

Lightweight pub/sub. BIRTH/DEATH/DATA/CMD message types.

## 🔧 LAYER 8: Modbus

Field protocol. Coils, registers, function codes.

## 📊 LAYER 9: KPIs

OEE = Availability x Performance x Quality. Target >85%.

## 🔀 CROSSWALKS

- ISA-95 ↔ ISA-88: WorkCenter=ProcessCell, WorkUnit=Unit
- ISA-95 ↔ OPC-UA: Equipment→Object, Property→Variable
- ISA-88 ↔ PackML: State machine subset mapping
- OPC-UA ↔ Sparkplug: Variable→Metric, Method→CMD

## 🎯 GOAL

- LAYER 0 defines how all layers are structured (self-describing)
- LAYER 1 provides base UDTs all standards share
- LAYER 2+ each standard compressed, UDT-first
- CROSSWALKS map between standards
- AGENTS: parse, expand, validate, crosswalk, generate
