# Polygons

Polygons are a common way to represent shapes. This document describes the different ways to represent polygons in the protobuf format.

## Point2D

Two dimensional point consisting of an x and y coordinates.

```proto
message Point2D {
  sint64 x = 1;
  sint64 y = 2;
}
```

## OpenPath

Simple path, otherwise revered to as a line-string. The path is not considered to be closed, the first point is not connected to the last point.

![OpenPath](resources/polygons/open_path.png)

```proto
message OpenPath {
  repeated Point2D path = 1;
}
```

## ClosedPath

`ClosedPath`, this message is different from the [`OpenPath`](#openpath) in that the path must be interpreted as being "closed"; the last point in the path is connected to the first point. The interior of the path is not considered to be part of the polygon.

![ClosedPath](resources/polygons/closed_path.png)

```proto
message ClosedPath {
  repeated Point2D path = 1;
}
```

## FilledPath

Similar to [`ClosedPath`](#ClosedPath), but the interior is considered to be part of the shape.

![FilledPath](resources/polygons/filled_path.png)

```proto
message FilledPath {
  repeated Point2D path = 1;
}
```

## Polygon

An outline with (possibly) multiple holes. Here point that is inside the outline, and is not inside one of the holes is considered to be part of the polygon.

![Polygon](resources/polygons/polygon.png)

```proto
message Polygon {
  FilledPath outline = 1;
  repeated FilledPath holes = 2;
}
```

## Polygons

Multiple (possibly nested) polygons. Its not possible to express a nesting structure within this dataype, if this is needed see the [`PolyTree`](#polytree) datastructures.

![Polygons](resources/polygons/polygons.png)

```proto
message Polygons {
  repeated Polygon polygons = 1;
}
```

## PolyTree

A data structure describing the nesting structure of nested of polygons/paths.

![PolyTree](resources/polygons/poly_tree.png)

![PolyTree - Tree view](resources/polygons/poly_tree_tree.png)

```proto
message PolyTreeRoot {
  repeated FilledPolyTreeNode polygons = 1;
  repeated ClosedPolyTreeNode closed_paths = 2;
  repeated OpenPath open_paths = 3;
}

message FilledPolyTreeNode {
  FilledPath outline = 1;
  repeated HolePolyTreeNode holes = 2;
}

message HolePolyTreeNode {
  FilledPath outline = 1;
  PolyTreeRoot children = 2;
}

message ClosedPolyTreeNode {
  OpenPath outline = 1;
  PolyTreeRoot children = 2;
}
```