import open3d as o3d

def main():
    try:
        pcd = o3d.io.read_point_cloud("sample.pcd")
        print("Point cloud loaded")
        o3d.visualization.draw_geometries([pcd])
    except:
        print("No point cloud file found")

if __name__ == "__main__":
    main()
