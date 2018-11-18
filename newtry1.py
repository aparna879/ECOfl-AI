import pandas as pd, numpy as np, matplotlib.pyplot as plt, time
from sklearn.cluster import DBSCAN
from sklearn import metrics
from geopy.distance import great_circle
from shapely.geometry import MultiPoint

def cluster():
    connection = sqlite3.connect("safai.db")
    cursor = connection.cursor()
    cursor.execute('SELECT lattitude, longitude from report')
    res = cursor.fetchall()
    connection.commit()
# define the number of kilometers in one radian
    kms_per_radian = 6371.0088
    

# load the data set
    temp_mat=[]
# listofc=[]
    for x in res:
        temp_mat.append([x[0],x[1]])
    coords=np.array(temp_mat)

# define epsilon as 1.5 kilometers, converted to radians for use by haversine
    epsilon = 500/ kms_per_radian

    
    db = DBSCAN(eps=epsilon, min_samples=2, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    cluster_labels = db.labels_

# get the number of clusters
    num_clusters = len(set(cluster_labels))

# all done, print the outcome
# message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'
# print(message.format(len(df), num_clusters, 100*(1 - float(num_clusters) / len(df)), time.time()-start_time))
# print('Silhouette coefficient: {:0.03f}'.format(metrics.silhouette_score(coords, cluster_labels)))

# turn the clusters in to a pandas series, where each element is a cluster of points
    clusters = pd.Series([coords[cluster_labels==n] for n in range(num_clusters)])

    def get_centermost_point(cluster):
        centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
        centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
        return tuple(centermost_point)

    centermost_points = clusters.map(get_centermost_point)

    lats, lons = zip(*centermost_points)

    print(lats)
#print(lons)


# from these lats/lons create a new df of one representative point for each cluster
# rep_points = pd.DataFrame({'lon':lons, 'lat':lats})
# rep_points.tail()

# # pull row from original data set where lat/lon match the lat/lon of each row of representative points
# # that way we get the full details like city, country, and date from the original dataframe
# rs = rep_points.apply(lambda row: df[(df['lat']==row['lat']) & (df['lon']==row['lon'])].iloc[0], axis=1)
# rs.to_csv('summer-travel-gps-dbscan.csv', encoding='utf-8')
# rs.tail()


# # plot the final reduced set of coordinate points vs the original full set
# fig, ax = plt.subplots(figsize=[10, 6])
# rs_scatter = ax.scatter(rs['lon'], rs['lat'], c='#99cc99', edgecolor='None', alpha=0.7, s=120)
# df_scatter = ax.scatter(df['lon'], df['lat'], c='k', alpha=0.9, s=3)
# ax.set_title('Full data set vs DBSCAN reduced set')
# ax.set_xlabel('Longitude')
# ax.set_ylabel('Latitude')
# ax.legend([df_scatter, rs_scatter], ['Full set', 'Reduced set'], loc='upper right')
# plt.show()