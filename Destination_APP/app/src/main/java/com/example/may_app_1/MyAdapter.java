package com.example.may_app_1;

import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Filter;
import android.widget.Filterable;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.List;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> implements Filterable {
    private Context context;
    private List<MainViewModel> myList;
    private List<MainViewModel> myListFull;

    public MyAdapter(Context context, List<MainViewModel> myList) {
        this.context = context;
        this.myList = myList;
        myListFull = new ArrayList<>(myList);
    }

    @NonNull
    @Override
    public MyAdapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(context).inflate(R.layout.recylclerview_main,parent,false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull MyAdapter.MyViewHolder holder, int position) {
        MainViewModel mainViewModel = myList.get(position);

        holder.mprofile.setText(mainViewModel.profile);
        holder.mcompany.setText(mainViewModel.name);


    }


    @Override
    public int getItemCount() {
        return myList.size();
    }

    class MyViewHolder extends RecyclerView.ViewHolder implements View.OnClickListener{
        TextView mprofile;
        TextView mcompany;
        ImageView mImageView;
        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            mprofile = itemView.findViewById(R.id.profile_name);
            mcompany = itemView.findViewById(R.id.company_name);
            mImageView = itemView.findViewById(R.id.imageview);
            itemView.setOnClickListener(this);
        }
        @Override
        public void onClick(View view) {
            int p = getAdapterPosition();
            MainViewModel mainViewModel = myList.get(p);
            Intent intent = new Intent(context,OrderActivity.class);
            intent.putExtra("name",mainViewModel.name);
            intent.putExtra("link",mainViewModel.link);
            intent.putExtra("desc",mainViewModel.desc);
            intent.putExtra("profile",mainViewModel.profile);
            intent.putExtra("thumb",mainViewModel.thumb);
            context.startActivity(intent);
        }
    }


    @Override
    public Filter getFilter() {
        return exampleFilter;
    }
    private Filter exampleFilter = new Filter() {
        @Override
        protected FilterResults performFiltering(CharSequence charSequence) {
            List<MainViewModel> filteredList = new ArrayList<>();
            if(charSequence==null || charSequence.length()==0){
                filteredList.addAll(myListFull);
            }
            else{
                String filterPattern = charSequence.toString().toLowerCase().trim();
                for(MainViewModel item:myListFull){
                    if(item.getName().toLowerCase().contains(filterPattern) || item.getProfile().toLowerCase().contains(filterPattern)){
                        filteredList.add(item);
                    }
                }
            }
            FilterResults res = new FilterResults();
            res.values=filteredList;
            return res;
        }

        @Override
        protected void publishResults(CharSequence charSequence, FilterResults filterResults) {
            myList.clear();
            myList.addAll((List)filterResults.values);
            notifyDataSetChanged();
        }
    };
}